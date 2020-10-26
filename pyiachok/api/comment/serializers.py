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
        fields = ('first_name',)


class ShowCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CommentModel
        # fields = ('rate', 'text', 'bill',)
        exclude = ('id', 'place', )

# class ShowCommentSerializer(serializers.ModelSerializer):
#
#         rate = serializers.IntegerField(max_length=30)
#         text = serializers.CharField(max_length=30)
#         bill = serializers.ImageField()
#         first_name = serializers.CharField(max_length=30)
