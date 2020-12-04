from rest_framework import serializers
from .models import ChatCommentModel
from django.contrib.auth import get_user_model
from ..user_profile.serializers import ShowUserSerializer


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCommentModel
        fields = ('text', )


class ShowMessageSerializer(serializers.ModelSerializer):
    users = ShowUserSerializer()

    class Meta:
        model = ChatCommentModel
        exclude = ('pyiachok_id',)


class EditMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCommentModel
        fields = ('text', 'edited')
