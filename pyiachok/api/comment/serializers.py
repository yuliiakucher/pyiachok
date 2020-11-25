from rest_framework import serializers
from .models import CommentModel
from django.contrib.auth import get_user_model

from ..models import ProfileModel

User = get_user_model()


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('rate', 'text', 'bill',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('photo',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')


class ShowCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CommentModel
        exclude = ('place', )


