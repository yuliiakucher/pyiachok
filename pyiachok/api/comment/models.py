import os

from django.db import models
from django.core.validators import MaxValueValidator
from ..models import ProfileModel
from ..place.models import PlaceModel, User


class CommentModel(models.Model):
    class Meta:
        db_table = 'comment'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    place = models.ForeignKey(PlaceModel, related_name='comments', on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MaxValueValidator(10)])
    text = models.TextField(max_length=800)
    bill = models.ImageField(upload_to=os.path.join('comments', 'img'), default='')
    date = models.DateTimeField(auto_now=True)


