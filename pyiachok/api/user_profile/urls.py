from .views import ProfileView, ShowFavouritePlacesView, DeleteFavPlaceView, ShowStatisticView, ShowPlaceByUserView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/edit/', ProfileView.as_view()),
    path('profile/fav_places', ShowFavouritePlacesView.as_view()),
    path('profile/del-from-fav/<int:place_id>/', DeleteFavPlaceView.as_view()),
    path('place/<int:place_id>/statistic', ShowStatisticView.as_view()),
    path('profile/owned-places', ShowPlaceByUserView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
