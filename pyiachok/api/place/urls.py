from django.urls import path
from .views import ShowPlaceView, CreatePlaceView

urlpatterns = [
    path('<int:pk>/', ShowPlaceView.as_view()),
    path('', CreatePlaceView.as_view()),
]
