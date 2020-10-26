from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CreateCommentSerializer, ShowCommentSerializer
from .models import CommentModel


class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, pk):
        serializer = CreateCommentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Укажите корректные данные'}, status=400)
        new_comment = CommentModel.objects.create(**serializer.data, place_id=pk, user_id=request.user.id)
        new_comment.save()
        return Response({'message': 'Комментарий отправлен'}, status=201)


class ShowCommentsView(APIView):
    @staticmethod
    def get(request, pk):
        comment = CommentModel.objects.filter(place_id=pk)
        if not comment:
            return Response({'message': 'Некорректные данные заведения'}, status=400)
        serializer = ShowCommentSerializer(comment, many=True)
        return Response(serializer.data, status=200)
