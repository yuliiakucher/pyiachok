from .views import ProfileView, ShowFavouritePlacesView, DeleteFavPlaceView, ShowStatisticView
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

urlpatterns = [
    path('profile/edit/', ProfileView.as_view()),
    path('profile/fav_places', ShowFavouritePlacesView.as_view()),
    path('profile/del-from-fav/<int:place_id>/', DeleteFavPlaceView.as_view()),
    path('place/<int:place_id>/statistic', ShowStatisticView.as_view()),
]
