from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import PlaceModel, TagModel, SpecificityModel, TypeModel, ViewStatisticModel, CoordinatesModel, PhotoModel
from .serializers import ShowPlaceSerializer, CreatePlaceSerializer, TagSerializer, TypeSerializer, \
    SpecificitiesSerializer, EditPlaceSerializer, CoordinatesSerializer, RateSerializer, PhotoSerializer
from ..comment.models import CommentModel


class CreatePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        data = CreatePlaceSerializer(data=request.data, context={'user': request.user})
        if not data.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        data.save()

        return Response({'message': 'Заявка на создание заведения успешно сформирована'}, status=201)


class AddPhotoView(APIView):
    permission_classes = [IsAuthenticated]
    """URL place/<place_id>/add-photo/"""

    @staticmethod
    def post(request, place_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        print(request.FILES)
        serializer = PhotoSerializer(data=request.FILES)
        if not serializer.is_valid() or not place:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        elif PlaceModel.objects.filter(admins=request.user, id=place_id).first() is None:
            return Response({'message': 'У Вас нет доступа'}, status=400)
        serializer.save(places=place)
        return Response({'message': 'Фото успешно добавлено'}, status=200)


class EditPlaceView(APIView):
    """ URL place/place_id/edit/"""

    # permission_classes = [IsAuthenticated]

    @staticmethod
    def patch(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        data = request.data
        if 'coordinates' in request.data:
            coordinates = data.pop('coordinates')
            place_coordinates = CoordinatesModel.objects.filter(place=place).first()
            serializer = CoordinatesSerializer(place_coordinates, data=coordinates)
            if not serializer.is_valid():
                return Response({'message': 'Укажите корректные данные'}, status=400)
            serializer.save()
        serializer = EditPlaceSerializer(place, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        serializer.save()
        return Response({'message': 'Изменения успешно сохранены'}, status=200)


class ShowAllPlaces(APIView):
    """URL place/all"""

    @staticmethod
    def get(request):
        places = PlaceModel.objects.order_by('-rating')
        params = request.query_params.copy()
        tags = params.pop('tag', [])
        spec = params.pop('spec', [])
        place_type = request.query_params.get('type', None)
        sort_abc = request.query_params.get('sort_abc', None)
        if place_type:
            places = places.filter(type=place_type)
        if tags:
            for i in tags:
                places = places.filter(tags=i)
        if spec:
            for i in spec:
                places = places.filter(specificities=i)
        if sort_abc:
            if sort_abc == 'True':
                places = places.order_by('name')
            else:
                places = places.order_by('-name')
        page = request.query_params.get('page', None)
        index = int(page) * 10 - 10
        places = places[index: index + 11]
        count = places.count()
        serializer = ShowPlaceSerializer(places, many=True)
        return Response({'data': serializer.data, 'count': count})


class SearchPlaceByName(APIView):
    """URL place/search"""

    @staticmethod
    def get(request):
        name = request.query_params.get('name', None)
        place = PlaceModel.objects.filter(name__istartswith=name).first()
        if not place:
            return Response({'message': 'По вашему запросу ничего не найдено'}, status=400)
        serializer = ShowPlaceSerializer(place)
        return Response(serializer.data)


class ShowTopPlacesView(APIView):
    """URl place/top"""

    @staticmethod
    def get(request):
        filtered_places = PlaceModel.objects.order_by('-statistic_views').all()[:10]
        filtered_serializer = ShowPlaceSerializer(filtered_places, many=True)
        return Response(filtered_serializer.data)


class ShowPlaceView(APIView):

    @staticmethod
    def get(request, pk):
        place = PlaceModel.objects.get(id=pk)
        serializer = ShowPlaceSerializer(place)
        place.statistic_views += 1
        place.save()
        view = ViewStatisticModel.objects.create(place=place)
        view.save()
        return Response({'data': serializer.data})


class AllAdditionalInfoView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        tags_model = TagModel.objects.all()
        tags = TagSerializer(tags_model, many=True)
        spec_model = SpecificityModel.objects.all()
        spec = SpecificitiesSerializer(spec_model, many=True)
        type_model = TypeModel.objects.all()
        type = TypeSerializer(type_model, many=True)
        return Response({'tags': tags.data, 'spec': spec.data, 'type': type.data})


class AddAdminView(APIView):
    """"URL place/place_id/add-admin"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        admin = User.objects.get(email=request.data['email'])
        owner = PlaceModel.objects.filter(id=place_id, owner_id_id=request.user.id).first()
        if not place or not admin or owner is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        place.admins.add(admin)

        place.save()
        return Response({'message': 'Админ успешно добавлен'}, status=200)


class AddPlaceToFavourites(APIView):
    """URL place/<place_id>/add-to-fave/"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        user = request.user
        user.favourites_places.add(place)
        user.save()
        return Response({'message': 'Заведение добавлено в избранное'}, status=200)


class CreateSpecificityView(APIView):
    """URL specificity/create"""

    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = SpecificitiesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        data = SpecificityModel(**serializer.data)
        data.save()
        return Response({'message': 'Особенность сохранена'}, 201)


class AddSpecificityView(APIView):
    """URL place/<place_id>/spec-add/<spec_id>"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, place_id, spec_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        spec = SpecificityModel.objects.filter(id=spec_id).first()
        if PlaceModel.objects.filter(admins=request.user, id=place_id).first() is None:
            return Response({'message', 'У вас нет доступа'}, 400)
        place.specificities.add(spec)
        place.save()
        return Response({'message': 'Особенность добавлена'}, 200)


class DeleteSpecificityView(APIView):
    """URL place/<place_id>/specificity/<spec_id>/delete"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, place_id, spec_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        if PlaceModel.objects.filter(admins=request.user, id=place_id).first() is None:
            return Response({'message', 'У вас нет доступа'}, 400)
        place.specificities.remove(spec_id)
        place.save()
        return Response({'message': 'Особенность удалена'}, 200)


class CreateTagView(APIView):
    """URL tag/create"""

    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = TagSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        data = TagModel(**serializer.data)
        data.save()
        return Response({'message': 'Тэг сохранен'}, 201)


class AddTagView(APIView):
    """URL place/<place_id>/tag-add/<spec_id>"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, place_id, tag_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        tag = TagModel.objects.filter(id=tag_id).first()
        if PlaceModel.objects.filter(admins=request.user, id=place_id).first() is None:
            return Response({'message', 'У вас нет доступа'}, 400)
        place.tags.add(tag)
        place.save()
        return Response({'message': 'Тэг добавлена'}, 200)


class DeleteTagView(APIView):
    """URL place/<place_id>/tag/<tag_id>/delete"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, place_id, tag_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        if PlaceModel.objects.filter(admins=request.user, id=place_id).first() is None:
            return Response({'message', 'У вас нет доступа'}, 400)
        place.tags.remove(tag_id)
        place.save()
        return Response({'message': 'Тэг удален'}, 200)
