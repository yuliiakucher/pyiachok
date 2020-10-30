from rest_framework import serializers
from .models import NewsModel, NewsTypeModel


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTypeModel
        fields = ('type', 'id')


class CreateNewsSerializer(serializers.ModelSerializer):
    type = NewsTypeSerializer(read_only=True)

    class Meta:
        model = NewsModel
        exclude = ('id', 'place_id')



