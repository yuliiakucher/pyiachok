from .views import ProfileView
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

urlpatterns = [
    path('profile/edit/', views.ProfileView.as_view())
]
