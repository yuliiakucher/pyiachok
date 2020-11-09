from django.urls import path
from .views import CreateNewsView, ShowNewsTypeView, ShowTopNewsView

urlpatterns = [
    path('place/<int:place_id>/add-news/', CreateNewsView.as_view()),
    path('news-type/all', ShowNewsTypeView.as_view()),
    path('news-top', ShowTopNewsView.as_view()),
]
