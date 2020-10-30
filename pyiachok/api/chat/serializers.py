from rest_framework import serializers
from .models import ChatCommentModel
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCommentModel
        fields = ('text', )


class ShowMessageSerializer(serializers.ModelSerializer):
    users = UserSerializer()

    class Meta:
        model = ChatCommentModel
        exclude = ('pyiachok_id',)


class EditMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCommentModel
        fields = ('text', 'edited')
