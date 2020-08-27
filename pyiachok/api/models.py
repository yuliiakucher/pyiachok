import os
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class NewsTypeModel(models.Model):
    class Meta:
        db_table = 'news_type'

    news_type = models.CharField(max_length=30)


class TagModel(models.Model):
    class Meta:
        db_table = 'tag'

    tag_name = models.CharField(max_length=30)


class SpecificityModel(models.Model):
    class Meta:
        db_table = 'specificity'

    specificity_name = models.CharField(max_length=30)


class TypeModel(models.Model):
    class Meta:
        db_table = 'type'

    type_name = models.CharField(max_length=30)




class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=30)


class PlaceModel(models.Model):
    class Meta:
        db_table = 'place'

    name = models.CharField(max_length=30, blank=False)
    tags = models.ManyToManyField(TagModel, related_name='places')
    specificities = models.ManyToManyField(SpecificityModel, related_name='places')
    address = models.CharField(max_length=50)
    contacts = models.CharField(max_length=70)
    statistic_views = models.IntegerField(default=0)
    type = models.ForeignKey(TypeModel, related_name='place', on_delete=models.CASCADE)
    passed_moderation = models.BooleanField(default=False)
    email = models.EmailField(max_length=30, unique=True)
    owner_id = models.ForeignKey(ProfileModel, related_name='owned_places', on_delete=models.CASCADE)
    fav = models.ManyToManyField(ProfileModel, related_name='favourites_places')
    admins = models.ManyToManyField(ProfileModel, related_name='moderated_places')


class PyiachokModel(models.Model):
    class Meta:
        db_model = 'pyiachok'

    date = models.DateTimeField()
    purpose = models.CharField(max_length=150)
    sex = models.CharField(validators=[RegexValidator('^([fma])$', 'only f/m/a')])
    number_of_people = models.IntegerField()
    payer = models.CharField(max_length=20)
    expenditures = models.IntegerField()
    public = models.BooleanField(default=True)
    participants = models.ManyToManyField(ProfileModel, related_name='active_pyiachky')
    requests = models.ManyToManyField(ProfileModel, related_name='pyiachok_requests')
    place_id = models.ForeignKey(PlaceModel, on_delete=models.CASCADE, related_name='pyiachky')


class ChatCommentModel(models.Model):
    class Meta:
        db_table = 'chat_comment'

    users = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='chat_comments')
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    pyiachok_id = models.ForeignKey(PyiachokModel, on_delete=models.CASCADE, related_name='chat_comments')


class NewsModel(models.Model):
    class Meta:
        db_table = 'news'

    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to=os.path.join('news', 'img'), default='')
    text = models.TextField(max_length=1000)
    type = models.ManyToManyField(NewsTypeModel, related_name='news')
    place_id = models.ForeignKey(PlaceModel, on_delete=models.CASCADE, related_name='news')

class PhotoModel(models.Model):
    class Meta:
        db_table = 'photos'

    photo = models.ImageField(upload_to=os.path.join('places', 'img'), default='')
    places = models.ForeignKey(PlaceModel, related_name='photos', on_delete=models.CASCADE)

class NewsDurationModel(models.Model):
    class Meta:
        db_table = 'news_duration'

    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    news = models.OneToOneField(NewsModel, on_delete=models.CASCADE, related_name='duration')


class CoordinatesModel(models.Model):
    class Meta:
        db_table = 'coordinates'

    lat = models.CharField(blank=False)
    lng = models.CharField(blank=False)
    place = models.OneToOneField(PlaceModel, on_delete=models.CASCADE, related_name='coordinates')


class ScheduleModel(models.Model):
    class Meta:
        db_table = 'schedule'

    mon_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    mon_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    tue_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    tue_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    wed_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    wed_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    thu_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    thu_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    fri_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    fri_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sat_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sat_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sun_open = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    sun_close = models.CharField(validators=[RegexValidator('^(([0-1]{0,1}[0-9])|(2[0-3])):[0-5]{0,1}[0-9]$')])
    place = models.OneToOneField(PlaceModel, on_delete=models.CASCADE, related_name='schedule')


class CommentModel(models.Model):
    class Meta:
        db_table = 'comment'

    user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='comments')
    place = models.ForeignKey(PlaceModel, related_name='comments', on_delete=models.CASCADE)
    rate = models.IntegerField(max_length=1)
    text = models.TextField(max_length=800)
    bill = models.IntegerField()
