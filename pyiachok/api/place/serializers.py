from rest_framework import serializers
from .models import PlaceModel, TagModel, SpecificityModel, ScheduleModel, CoordinatesModel, TypeModel, PhotoModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('id', 'tag_name',)


class SpecificitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificityModel
        fields = ('id', 'specificity_name',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeModel
        fields = ('id', 'type_name',)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        exclude = ('place',)


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

    def create(self, validated_data):

        type = validated_data.pop('type')
        specificities = validated_data.pop('specificities', [])
        tags = validated_data.pop('tags', [])
        schedule = validated_data.pop('schedule')
        coordinates = validated_data.pop('coordinates')
        exist = TypeModel.objects.filter(type_name__iexact=type['type_name']).first()
        creating_type = exist if exist else TypeModel.objects.create(**type)
        if exist:
            instance = PlaceModel.objects.create(owner_id_id=self.context['user'].id,
                                                 type=exist, **validated_data, )

        else:
            instance = PlaceModel.objects.create(owner_id_id=self.context['user'].id,
                                                 type=creating_type,
                                                 **validated_data)

        for item in specificities:
            all_specificities = SpecificityModel.objects.all()
            new_specificities = []
            for i in all_specificities:
                new_specificities.append(i.specificity_name)
            if item['specificity_name'] not in new_specificities:
                data = SpecificityModel.objects.create(**item)
                instance.specificities.add(data)
        for item in tags:
            all_tags = TagModel.objects.all()
            new_tags = []
            for i in all_tags:
                new_tags.append(i.tag_name)
            if item['tag_name'] not in new_tags:
                data = TagModel.objects.create(**item)
                instance.tags.add(data)
        ScheduleModel.objects.create(**schedule, place_id=instance.id)
        CoordinatesModel.objects.create(**coordinates, place_id=instance.id)
        return instance
