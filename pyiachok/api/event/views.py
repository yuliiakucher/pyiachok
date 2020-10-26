from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CreatePyiachokSerializer, ShowPyiachokSerializer
from ..place.models import PlaceModel
from .models import PyiachokModel


class CreatePyiachokView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, pk):
        print(request.data)
        serializer = CreatePyiachokSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        new_event = PyiachokModel.objects.create(**serializer.data, place_id_id=pk)
        print(new_event.participants)
        new_event.participants.add(request.user)
        new_event.save()
        return Response({'message': 'Пиячок успешно создан'}, status=201)


class ShowPyiachokView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, sk, pk):
        chosen_event = PyiachokModel.objects.get(id=sk)
        if not chosen_event:
            return Response({'message': 'Некорректные данные заведения или пиячка'}, status=400)
        serializer = ShowPyiachokSerializer(chosen_event)
        return Response(serializer.data, status=200)

    @staticmethod
    def patch(request, sk, pk):
        user = request.user
        event = PyiachokModel.objects.get(id=sk)
        if not event:
            return Response({'message': 'Некорректное идентификатор заведения'}, status=400)
        event.participants.add(user)
        event.save()
        return Response({'message': f'пользователь {user.username} добавлен в пиячок'}, status=200)
