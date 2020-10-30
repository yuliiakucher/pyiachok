from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import NewsModel, NewsTypeModel
from ..place.models import PlaceModel
from .serializers import CreateNewsSerializer, NewsTypeSerializer


class CreateNewsView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        serializer = CreateNewsSerializer(data=request.data)
        if not serializer.is_valid() or not place or PlaceModel.objects.filter(admins=request.user).first() is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        news = NewsModel.objects.create(**serializer.data, place_id=place)
        news.save()
        return Response({'message': 'Новость создана'}, status=201)


class ShowNewsTypeView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        types = NewsTypeModel.objects.all()
        serializer = NewsTypeSerializer(types, many=True)
        return Response({'types': serializer.data})
