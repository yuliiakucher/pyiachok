from rest_framework import serializers
from rest_framework.serializers import IntegerField
from .models import PlaceModel, TagModel, SpecificityModel, ScheduleModel, CoordinatesModel, TypeModel, PhotoModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('id', 'tag_name',)


class SpecificitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificityModel
        fields = ('id', 'specificity_name',)
        # extra_kwargs = {'id': {'required': False}}


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


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('photo',)


class ShowPlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    specificities = SpecificitiesSerializer(many=True)
    type = TypeSerializer()
    schedule = ScheduleSerializer()
    coordinates = CoordinatesSerializer()

    class Meta:
        model = PlaceModel
        fields = ('id', 'name', 'address', 'photos',
                  'contacts', 'email',
                  'tags', 'specificities', 'type', 'schedule', 'coordinates', 'statistic_views')
        extra_kwargs = {'photos': {'required': False},
                        'schedule': {'required': False},
                        'coordinates': {'required': False},
                        }


class EditPlaceSerializer(serializers.ModelSerializer):
    type = TypeSerializer(required=False, read_only=True)
    schedule = ScheduleSerializer(required=False, read_only=True)

    # coordinates = CoordinatesSerializer(required=False, read_only=True)

    class Meta:
        model = PlaceModel
        fields = ('name', 'email', 'address', 'contacts', 'type', 'schedule')


class CreatePlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    specificities = SpecificitiesSerializer(many=True)
    type = TypeSerializer()
    schedule = ScheduleSerializer()
    coordinates = CoordinatesSerializer()
    photos = PhotoSerializer()

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
        photos = validated_data.pop('photos')
        print(photos)
        exist = TypeModel.objects.filter(type_name__iexact=type['type_name']).first()
        creating_type = exist if exist else TypeModel.objects.create(**type)
        if exist:
            instance = PlaceModel.objects.create(owner_id_id=self.context['user'].id,
                                                 type=exist, **validated_data, )
            instance.admins.add(self.context['user'])
        else:
            instance = PlaceModel.objects.create(owner_id_id=self.context['user'].id,
                                                 type=creating_type,
                                                 **validated_data)
            instance.admins.add(self.context['user'])
        for item in specificities:
            all_specificities = SpecificityModel.objects.all()
            new_specificities = []
            for i in all_specificities:
                new_specificities.append(i.specificity_name)
            if item['specificity_name'] not in new_specificities:
                data = SpecificityModel.objects.create(**item)
                instance.specificities.add(data)
            else:
                new_data = SpecificityModel.objects.get(specificity_name=item['specificity_name'])
                instance.specificities.add(new_data)
            new_data = SpecificityModel.objects.get(specificity_name=item['specificity_name'])
            instance.specificities.add(new_data)
        for item in tags:
            all_tags = TagModel.objects.all()
            new_tags = []
            for i in all_tags:
                new_tags.append(i.tag_name)
            if item['tag_name'] not in new_tags:
                data = TagModel.objects.create(**item)
                instance.tags.add(data)
            else:
                new_data = TagModel.objects.get(tag_name=item['tag_name'])
                instance.tags.add(new_data)
        ScheduleModel.objects.create(**schedule, place_id=instance.id)
        CoordinatesModel.objects.create(**coordinates, place_id=instance.id)
        return instance


class RateSerializer(serializers.ModelSerializer):
    rate = IntegerField()

    class Meta:
        model = PlaceModel
        fields = ('id', 'name', 'rate')
