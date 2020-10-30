from django.urls import path
from .views import CreateNewsView, ShowNewsTypeView

urlpatterns = [
    path('place/<int:place_id>/add-news/', CreateNewsView.as_view()),
    path('news-type/all', ShowNewsTypeView.as_view()),
]
