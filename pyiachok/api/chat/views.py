from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CreateMessageSerializer, ShowMessageSerializer
from .models import ChatCommentModel
from ..event.models import PyiachokModel


class CreateMessageView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, pk, sk):
        serializer = CreateMessageSerializer(data=request.data)
        event = PyiachokModel.objects.filter(id=sk).first()
        if not serializer.is_valid() or PyiachokModel.objects.filter(participants=request.user, id=sk).first() is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        new_msg = ChatCommentModel.objects.create(**serializer.data, pyiachok_id=event, users=request.user)
        new_msg.save()
        return Response({'message': 'Сообщение отправлено'}, status=201)


class ShowMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, pk, sk):
        messages = ChatCommentModel.objects.filter(pyiachok_id=sk)
        if PyiachokModel.objects.filter(participants=request.user, id=sk).first() is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        serializer = ShowMessageSerializer(messages, many=True)
        return Response(serializer.data, status=200)
