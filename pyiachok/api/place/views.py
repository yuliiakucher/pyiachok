from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import ProfileModel, User
from .models import PlaceModel
from .serializers import ShowPlaceSerializer, CreatePlaceSerializer


class CreatePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        data = CreatePlaceSerializer(data=request.data, context={'user': request.user})
        if not data.is_valid():
            return Response(data.errors, status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'message': 'Application for place registration is created'}, status=201)


class ShowPlaceView(APIView):

    @staticmethod
    def get(request, pk):
        place = PlaceModel.objects.get(id=pk)
        serializer = ShowPlaceSerializer(place)
        return Response(serializer.data)
