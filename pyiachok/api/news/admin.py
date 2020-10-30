from django.contrib import admin
from .models import NewsModel, NewsTypeModel

admin.site.register(NewsModel)
admin.site.register(NewsTypeModel)
