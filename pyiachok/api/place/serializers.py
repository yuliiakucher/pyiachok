from rest_framework import serializers
from .models import PlaceModel, TagModel, SpecificityModel, ScheduleModel, CoordinatesModel, TypeModel, PhotoModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('tag_name',)


class SpecificitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificityModel
        fields = ('specificity_name',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeModel
        fields = ('type_name',)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        exclude = 'place'


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoordinatesModel
        fields = ('lat', 'lng')


class ShowPlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    specificities = SpecificitiesSerializer(many=True)
    type = TypeSerializer()
    schedule = ScheduleSerializer()
    coordinates = CoordinatesSerializer()

    class Meta:
        model = PlaceModel
        fields = ('name', 'address', 'photos',
                  'contacts', 'email',
                  'tags', 'specificities', 'type', 'schedule', 'coordinates')
        extra_kwargs = {'photos': {'required': False},
                        'schedule': {'required': False},
                        'coordinates': {'required': False},
                        }


class CreatePlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    specificities = SpecificitiesSerializer(many=True)
    type = TypeSerializer()

    class Meta:
        model = PlaceModel
        fields = ('name', 'address', 'photos',
                  'contacts', 'email',
                  'tags', 'specificities', 'type', 'schedule', 'coordinates')
        extra_kwargs = {'photos': {'required': False},
                        'schedule': {'required': False},
                        'coordinates': {'required': False},
                        }

    def create(self, validated_data):
        type = validated_data.pop('type')
        specificities = validated_data.pop('specificities', [])
        tags = validated_data.pop('tags')
        creating_type = TypeModel.objects.create(**type)
        instance = PlaceModel.objects.create(owner_id_id=self.context['user'].id,
                                             type=creating_type, **validated_data)
        for item in specificities:
            data = SpecificityModel.objects.create(**item)
            instance.specificities.add(data)
        for item in tags:
            data = TagModel.objects.create(**item)
            instance.tags.add(data)
        return instance
