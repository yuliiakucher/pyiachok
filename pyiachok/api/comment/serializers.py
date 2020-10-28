from rest_framework import serializers
from .models import CommentModel
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('rate', 'text', 'bill',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ShowCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CommentModel
        exclude = ('id', 'place', )


