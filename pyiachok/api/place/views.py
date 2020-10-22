from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import ProfileModel, User
from .models import PlaceModel, TagModel, SpecificityModel, TypeModel
from .serializers import ShowPlaceSerializer, CreatePlaceSerializer, TagSerializer, TypeSerializer, \
    SpecificitiesSerializer


class CreatePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        data = CreatePlaceSerializer(data=request.data, context={'user': request.user})
        if not data.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        data.save()
        return Response({'message': 'Заявка на создание заведения успешно сформирована'}, status=201)


class ShowAllPlaces(APIView):

    @staticmethod
    def get(self):
        places = PlaceModel.objects.all()
        serializer = ShowPlaceSerializer(places, many=True)
        return Response(serializer.data)


class ShowPlaceView(APIView):

    @staticmethod
    def get(pk):
        place = PlaceModel.objects.get(id=pk)
        serializer = ShowPlaceSerializer(place)
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