from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..models import ProfileModel
from .models import PlaceModel, TagModel, SpecificityModel, TypeModel, ViewStatisticModel
from .serializers import ShowPlaceSerializer, CreatePlaceSerializer, TagSerializer, TypeSerializer, \
    SpecificitiesSerializer, EditPlaceSerializer


class CreatePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        data = CreatePlaceSerializer(data=request.data, context={'user': request.user})
        if not data.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        data.save()

        return Response({'message': 'Заявка на создание заведения успешно сформирована'}, status=201)


class EditPlaceView(APIView):
    """ URL place/place_id/edit/"""
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def patch(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        serializer = EditPlaceSerializer(place, data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        serializer.save()
        return Response({'message': 'Изменения успешно сохранены'}, status=200)


class ShowAllPlaces(APIView):
    """place/all"""

    @staticmethod
    def get(request):
        tag = request.query_params.get('tag', None)
        if tag:
            filtered_places = PlaceModel.objects.filter(tags__tag_name=tag).all()
            filtered_serializer = ShowPlaceSerializer(filtered_places, many=True)
            return Response(filtered_serializer.data)
        places = PlaceModel.objects.all()
        serializer = ShowPlaceSerializer(places, many=True)
        return Response(serializer.data)


class ShowPlaceView(APIView):

    @staticmethod
    def get(request, pk):
        place = PlaceModel.objects.get(id=pk)
        serializer = ShowPlaceSerializer(place)
        place.statistic_views += 1
        place.save()
        view = ViewStatisticModel.objects.create(place=place)
        view.save()
        return Response(serializer.data)


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
    """"place/place_id/add-admin"""
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
    """place/<place_id>/add-to-fave/"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        user = request.user
        user.favourites_places.add(place)
        user.save()
        return Response({'message': 'Заведение добавлено в избранное'}, status=200)






