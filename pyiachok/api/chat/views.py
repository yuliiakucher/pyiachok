from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CreateMessageSerializer, ShowMessageSerializer, EditMessageSerializer
from .models import ChatCommentModel
from ..event.models import PyiachokModel


class CreateMessageView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, sk):
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
    def get(request, sk):
        messages = ChatCommentModel.objects.filter(pyiachok_id=sk)
        if PyiachokModel.objects.filter(participants=request.user, id=sk).first() is None:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        serializer = ShowMessageSerializer(messages, many=True)
        return Response(serializer.data, status=200)


class EditMessageView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def patch(request, msg_id):
        message = ChatCommentModel.objects.get(id=msg_id)
        serializer = EditMessageSerializer(message, data=request.data)
        if not serializer.is_valid() or message.users_id != request.user.id:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        message.edited = True
        message.save()
        serializer.save()
        return Response({'message': 'Сообщение отредактировано'}, status=200)


class DeleteMessageView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, msg_id):
        message = ChatCommentModel.objects.get(id=msg_id)
        if not message or message.users_id != request.user.id:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        message.delete()
        return Response({'message': 'Сообщение удалено'}, status=200)
