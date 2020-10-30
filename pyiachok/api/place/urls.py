from django.urls import path
from .views import ShowPlaceView, CreatePlaceView,AllAdditionalInfoView, ShowAllPlaces

urlpatterns = [
    path('place/<int:pk>/', ShowPlaceView.as_view()),
    path('place/create-place/', CreatePlaceView.as_view()),
    path('place/tags', AllAdditionalInfoView.as_view()),
    path('place/all', ShowAllPlaces.as_view())
]
