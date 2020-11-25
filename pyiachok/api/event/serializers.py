from rest_framework import serializers
from .models import PyiachokModel
from ..place.models import PlaceModel
from ..user_profile.serializers import ShowUserSerializer


class CreatePyiachokSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyiachokModel
        fields = ('date', 'purpose', 'sex', 'number_of_people', 'payer',
                  'expenditures')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceModel
        fields = ('id', 'name',)


class ShowPyiachokSerializer(serializers.ModelSerializer):
    place_id = PlaceSerializer()
    creator = ShowUserSerializer()
    participants = ShowUserSerializer(many=True)

    class Meta:
        model = PyiachokModel
        fields = '__all__'
