import os
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    photo = models.ImageField(upload_to=os.path.join('user', 'img'), default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sex = models.CharField(max_length=30)

    def __str__(self):
        return self.user
