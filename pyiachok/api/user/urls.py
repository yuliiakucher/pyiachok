
from django.contrib import admin
from django.urls import path, include
from .views import CreateProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/create', CreateProfileView, basename='user')
urlpatterns = router.urls

# urlpatterns = [
#     path('/all/', CreateProfileView.as_view()),
# ]
