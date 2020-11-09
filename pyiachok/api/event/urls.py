from django.urls import path
from .views import CreatePyiachokView, ShowPyiachokView, ShowAllPyiachokView, DeletePyiachokView

urlpatterns = [
    path('place/<int:pk>/create-event/', CreatePyiachokView.as_view()),
    path('event/<int:sk>/', ShowPyiachokView.as_view()),
    path('event/all', ShowAllPyiachokView.as_view()),
    path('event/<int:event_id>/delete', DeletePyiachokView.as_view()),
]
