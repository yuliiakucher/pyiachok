from django.urls import path
from .views import CreatePyiachokView, ShowPyiachokView, ShowAllPyiachokView, DeletePyiachokView, ShowAllEventsByPlace

urlpatterns = [
    path('place/<int:pk>/create-event/', CreatePyiachokView.as_view()),
    path('event/<int:sk>/', ShowPyiachokView.as_view()),
    path('event/all', ShowAllPyiachokView.as_view()),
    path('event/<int:event_id>/delete', DeletePyiachokView.as_view()),
    path('place/<int:place_id>/events', ShowAllEventsByPlace.as_view()),
]
