from rest_framework import serializers
from .models import PyiachokModel


class CreatePyiachokSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyiachokModel
        fields = ('date', 'purpose', 'sex', 'number_of_people', 'payer',
                  'expenditures')


class ShowPyiachokSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyiachokModel
        exclude = ('place_id', )
