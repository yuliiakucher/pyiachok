from rest_framework import serializers
from ..models import ProfileModel, User
from ..event.models import PyiachokModel
from ..place.models import PlaceModel


class ShowProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        # fields = ('photo', 'owned_places')
        fields = ('photo', )


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('photo', )


class PyiachokSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyiachokModel
        fields = ('active_pyiachky',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceModel
        fields = ('favourites_places', 'moderated_places')


class ShowUserSerializer(serializers.ModelSerializer):
    profile = ShowProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile')


class EditUserSerializer(serializers.ModelSerializer):
    profile = EditProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile',)
        extra_kwargs = {'first_name': {'required': False},
                        'last_name': {'required': False},
                        'email': {'required': False},
                        'profile': {'required': False},
                        }


class FavPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceModel
        fields = ('name', 'id')

