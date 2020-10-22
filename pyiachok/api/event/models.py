from django.db import models
from django.core.validators import RegexValidator
from ..models import ProfileModel
from ..place.models import PlaceModel


class PyiachokModel(models.Model):
    class Meta:
        db_table = 'pyiachok'

    date = models.DateTimeField()
    purpose = models.CharField(max_length=150)
    sex = models.CharField(max_length=1, validators=[RegexValidator('^([fma])$', 'only f/m/a')])
    number_of_people = models.IntegerField()
    payer = models.CharField(max_length=20)
    expenditures = models.IntegerField()
    participants = models.ManyToManyField(ProfileModel, related_name='active_pyiachky')
    place_id = models.ForeignKey(PlaceModel, on_delete=models.CASCADE, related_name='pyiachky')
