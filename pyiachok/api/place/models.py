import os
from django.db import models
from django.core.validators import RegexValidator
from ..user.models import ProfileModel


class TagModel(models.Model):
    class Meta:
        db_table = 'tag'

    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class SpecificityModel(models.Model):
    class Meta:
        db_table = 'specificity'

    specificity_name = models.CharField(max_length=30)

    def __str__(self):
        return self.specificity_name


class TypeModel(models.Model):
    class Meta:
        db_table = 'type'

    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class PlaceModel(models.Model):
    class Meta:
        db_table = 'place'

    name = models.CharField(max_length=30, blank=False)
    tags = models.ManyToManyField(TagModel, related_name='places')
    specificities = models.ManyToManyField(SpecificityModel, related_name='places')
    address = models.CharField(max_length=50)
    contacts = models.CharField(max_length=70)
    statistic_views = models.IntegerField(default=0)
    type = models.ForeignKey(TypeModel, related_name='place', on_delete=models.SET_NULL, null=True)
    passed_moderation = models.BooleanField(default=False)
    email = models.EmailField(max_length=30, unique=True)
    owner_id = models.ForeignKey(ProfileModel, related_name='owned_places', on_delete=models.CASCADE)
    fav = models.ManyToManyField(ProfileModel, related_name='favourites_places')
    admins = models.ManyToManyField(ProfileModel, related_name='moderated_places')

    def __str__(self):
        return self.name


class PhotoModel(models.Model):
    class Meta:
        db_table = 'photos'

    photo = models.ImageField(upload_to=os.path.join('places', 'img'), default='')
    places = models.ForeignKey(PlaceModel, related_name='photos', on_delete=models.CASCADE)


class CoordinatesModel(models.Model):
    class Meta:
        db_table = 'coordinates'

    lat = models.CharField(blank=False, max_length=20)
    lng = models.CharField(blank=False, max_length=20)
    place = models.OneToOneField(PlaceModel, on_delete=models.CASCADE, related_name='coordinates')


class ScheduleModel(models.Model):
    class Meta:
        db_table = 'schedule'

    mon_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    mon_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    tue_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    tue_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    wed_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    wed_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    thu_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    thu_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    fri_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    fri_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sat_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sat_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sun_open = models.CharField(max_length=20,
                                validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sun_close = models.CharField(max_length=20,
                                 validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    place = models.OneToOneField(PlaceModel, on_delete=models.CASCADE, related_name='schedule')
