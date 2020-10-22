from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CreatePyiachokSerializer
from ..place.models import PlaceModel
from .models import PyiachokModel


class CreatePyiachokView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, pk):
        data = CreatePyiachokSerializer(request.data).data
        new_event = PyiachokModel.objects.create(**data, place_id_id=pk)
        new_event.save()
        return Response({'message': 'Пиячок успешно создан'}, status=201)
        # if not data.is_valid():
        #     return Response({'message': 'Укажите корректные данные'}, status=400)
        # data.save()
        # return Response({'message': 'Пиячок успешно создан'}, status=201)


