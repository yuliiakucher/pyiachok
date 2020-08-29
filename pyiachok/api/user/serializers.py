from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ProfileModel

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile',)



