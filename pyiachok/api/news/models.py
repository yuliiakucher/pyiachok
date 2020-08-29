import os
from django.db import models
from ..place.models import PlaceModel


class NewsTypeModel(models.Model):
    class Meta:
        db_table = 'newstype'

    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class NewsModel(models.Model):
    class Meta:
        db_table = 'news'

    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to=os.path.join('news', 'img'), default='')
    text = models.TextField(max_length=1000)
    type = models.ForeignKey(NewsTypeModel, related_name='news', on_delete=models.SET_NULL, null=True)
    place_id = models.ForeignKey(PlaceModel, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.name


class NewsDurationModel(models.Model):
    class Meta:
        db_table = 'news_duration'

    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    news = models.OneToOneField(NewsModel, on_delete=models.CASCADE, related_name='duration')
