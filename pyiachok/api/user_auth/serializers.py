from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import ProfileModel

User = get_user_model()


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30, required=True)
    password = serializers.CharField(max_length=30, required=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    sex = serializers.CharField(max_length=30)




