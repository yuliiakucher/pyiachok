from django.urls import path
from .views import CreatePyiachokView, ShowPyiachokView

urlpatterns = [
    path('place/<int:pk>/create-event/', CreatePyiachokView.as_view()),
    path('event/<int:sk>/', ShowPyiachokView.as_view()),
]
