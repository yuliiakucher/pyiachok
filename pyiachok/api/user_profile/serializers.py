from rest_framework import serializers
from ..user_auth.models import ProfileModel, User
from ..event.models import PyiachokModel
from ..place.models import PlaceModel
from django.contrib.auth import get_user_model





class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('photo',)


class PyiachokSerializer(serializers.ModelSerializer):

    class Meta:
        model = PyiachokModel
        fields = ('active_pyiachky',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceModel
        fields = ('owned', 'favourites_places', 'moderated_places')


class UserSerializer(serializers.ModelSerializer):
    photo = ProfileSerializer(many=True)
    pyiachky = PyiachokSerializer(many=True)
    places = PlaceSerializer(many=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'photo', 'pyiachky', 'places')
