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
        serializer = CreatePyiachokSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        new_event = PyiachokModel.objects.create(**serializer.data, place_id_id=pk, creator=request.user)
        new_event.participants.add(request.user)
        new_event.save()
        return Response({'message': 'Пиячок успешно создан'}, status=201)


class DeletePyiachokView(APIView):
    """URL event/<event_id>/delete/"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, event_id):
        event = PyiachokModel.objects.filter(id=event_id).first()
        print(event.creator)
        if not event or event.creator != request.user:
            return Response({'message': 'У вас нет доступа'}, status=400)
        event.delete()
        return Response({'message': 'Пиячок удален'}, status=200)


class ShowPyiachokView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, sk):
        chosen_event = PyiachokModel.objects.filter(id=sk).first()
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


class ShowAllPyiachokView(APIView):
    """event/all"""

    @staticmethod
    def get(request):
        pyiachoks = PyiachokModel.objects.all()
        serialiser = ShowPyiachokSerializer(pyiachoks, many=True)
        return Response(serialiser.data)


class ShowAllEventsByPlace(APIView):
    """URL place/<place_id>/events"""

    @staticmethod
    def get(request, place_id):
        place = PlaceModel.objects.filter(id=place_id).first()
        pyiachoks = PyiachokModel.objects.filter(place_id=place)
        serialiser = ShowPyiachokSerializer(pyiachoks, many=True)
        return Response(serialiser.data)
