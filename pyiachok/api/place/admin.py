from django.contrib import admin
from .models import TagModel, SpecificityModel, TypeModel, PlaceModel, ScheduleModel, PhotoModel, CoordinatesModel

admin.site.register(TagModel)
admin.site.register(SpecificityModel)
admin.site.register(TypeModel)
admin.site.register(PlaceModel)
admin.site.register(ScheduleModel)
admin.site.register(PhotoModel)
admin.site.register(CoordinatesModel)





