from django.urls import path
from .views import ShowPlaceView, CreatePlaceView,AllAdditionalInfoView, ShowAllPlaces, AddAdminView

urlpatterns = [
    path('place/<int:pk>/', ShowPlaceView.as_view()),
    path('place/create-place/', CreatePlaceView.as_view()),
    path('place/tags', AllAdditionalInfoView.as_view()),
    path('place/all', ShowAllPlaces.as_view()),
    path('place/<int:place_id>/add-admin/', AddAdminView.as_view()),
]
