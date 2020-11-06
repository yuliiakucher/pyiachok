from django.urls import path
from .views import ShowPlaceView, CreatePlaceView, AllAdditionalInfoView, ShowAllPlaces, AddAdminView, \
    AddPlaceToFavourites, EditPlaceView, CreateSpecificityView, CreateTagView, DeleteSpecificityView, DeleteTagView, \
    AddSpecificityView, AddTagView

urlpatterns = [
    path('place/<int:pk>/', ShowPlaceView.as_view()),
    path('place/create-place/', CreatePlaceView.as_view()),
    path('place/tags', AllAdditionalInfoView.as_view()),
    path('place/all', ShowAllPlaces.as_view()),
    path('place/<int:place_id>/add-admin/', AddAdminView.as_view()),
    path('place/<int:place_id>/add-to-fave/', AddPlaceToFavourites.as_view()),
    path('place/<int:place_id>/edit/', EditPlaceView.as_view()),
    path('specificity/create', CreateSpecificityView.as_view()),
    path('tag/create', CreateTagView.as_view()),
    path('place/<int:place_id>/specificity/<int:spec_id>/delete', DeleteSpecificityView.as_view()),
    path('place/<int:place_id>/tag/<int:tag_id>/delete', DeleteTagView.as_view()),
    path('place/<int:place_id>/spec-add/<int:spec_id>/', AddSpecificityView.as_view()),
    path('place/<int:place_id>/tag-add/<int:tag_id>/', AddTagView.as_view()),
]
