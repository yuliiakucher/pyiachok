from django.urls import path
from .views import ShowPlaceView, CreatePlaceView,AllAdditionalInfoView, ShowAllPlaces

urlpatterns = [
    path('<int:pk>/', ShowPlaceView.as_view()),
    path('', CreatePlaceView.as_view()),
    path('tags', AllAdditionalInfoView.as_view()),
    path('all', ShowAllPlaces.as_view())
]
