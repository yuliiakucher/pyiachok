from django.contrib import admin
from .models import NewsModel, NewsDurationModel, NewsTypeModel

admin.site.register(NewsModel)
admin.site.register(NewsDurationModel)
admin.site.register(NewsTypeModel)
