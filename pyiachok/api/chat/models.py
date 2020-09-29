from django.db import models

from ..event.models import PyiachokModel
from ..models import ProfileModel


class ChatCommentModel(models.Model):
    class Meta:
        db_table = 'chat_comment'

    users = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='chat_comments')
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    pyiachok_id = models.ForeignKey(PyiachokModel, on_delete=models.CASCADE, related_name='chat_comments')
