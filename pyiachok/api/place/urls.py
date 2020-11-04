from django.urls import path
from .views import ShowPlaceView, CreatePlaceView,AllAdditionalInfoView, ShowAllPlaces, AddAdminView, \
    AddPlaceToFavourites, EditPlaceView

urlpatterns = [
    path('place/<int:pk>/', ShowPlaceView.as_view()),
    path('place/create-place/', CreatePlaceView.as_view()),
    path('place/tags', AllAdditionalInfoView.as_view()),
    path('place/all', ShowAllPlaces.as_view()),
    path('place/<int:place_id>/add-admin/', AddAdminView.as_view()),
    path('place/<int:place_id>/add-to-fave/', AddPlaceToFavourites.as_view()),
    path('place/<int:place_id>/edit/', EditPlaceView.as_view()),
]
