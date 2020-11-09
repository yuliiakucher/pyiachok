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


class EditCommentView(APIView):
    """URl comment/<comment_id>/edit"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def patch(request, comment_id):
        comment = CommentModel.objects.filter(id=comment_id).first()
        serializer = CreateCommentSerializer(comment, data=request.data)
        if not serializer.is_valid() or comment.user_id != request.user.id:
            return Response({'message': 'Укажите корректные данные'}, status=400)
        comment.save()
        serializer.save()
        return Response({'message': 'Комментарий отредактирован'}, status=200)


class DeleteCommentView(APIView):
    """URl comment/<comment_id>/delete"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def delete(request, comment_id):
        comment = CommentModel.objects.filter(id=comment_id).first()
        if not comment or comment.user_id != request.user.id:
            return Response({'message': 'У вас нет доступа'}, status=400)
        comment.delete()
        return Response({'message': 'Комментарий удален'}, status=200)



class ShowCommentsView(APIView):
    @staticmethod
    def get(request, pk):
        comment = CommentModel.objects.filter(place_id=pk)
        if not comment:
            return Response({'message': 'Некорректные данные заведения'}, status=400)
        serializer = ShowCommentSerializer(comment, many=True)
        return Response(serializer.data, status=200)
