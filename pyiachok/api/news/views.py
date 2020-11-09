from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import NewsModel, NewsTypeModel
from ..place.models import PlaceModel
from .serializers import CreateNewsSerializer, NewsTypeSerializer, ShowTopNewsSerializer


class CreateNewsView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, place_id):
        place = PlaceModel.objects.get(id=place_id)
        type = NewsTypeModel.objects.get(id=request.data['type'])
        data = request.data
        new_data = data.pop('type')
        serializer = CreateNewsSerializer(data=data)
        if not serializer.is_valid() or not place or PlaceModel.objects.filter(admins=request.user).first() is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        news = NewsModel.objects.create(**serializer.data, place_id=place, type=type)
        news.save()
        return Response({'message': 'Новость создана'}, status=201)


class ShowNewsTypeView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        types = NewsTypeModel.objects.all()
        serializer = NewsTypeSerializer(types, many=True)
        return Response({'types': serializer.data})


class ShowTopNewsView(APIView):
    """URL /news-top/"""
    @staticmethod
    def get(request):
        type = request.query_params.get('type', None)
        if type and type == 'news':
            filtered_news = NewsModel.objects.order_by('id').all().filter(type=1)[:3]
            filtered_serializer = ShowTopNewsSerializer(filtered_news, many=True)
            return Response(filtered_serializer.data, 200)
        elif type and type == 'promotion':
            filtered_news = NewsModel.objects.order_by('id').all().filter(type=2)[:3]
            filtered_serializer = ShowTopNewsSerializer(filtered_news, many=True)
            return Response(filtered_serializer.data, 200)
        elif type and type == 'event':
            filtered_news = NewsModel.objects.order_by('id').all().filter(type=3)[:3]
            filtered_serializer = ShowTopNewsSerializer(filtered_news, many=True)
            return Response(filtered_serializer.data, 200)
