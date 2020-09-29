from django.urls import path
from . import views
from .views import CreateProfileView

urlpatterns = [
    path('register/', views.CreateProfileView.as_view())
]

