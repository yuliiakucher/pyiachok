from django.urls import path
from .views import CreatePyiachokView

urlpatterns = [
    path('place/<int:pk>/create_event/', CreatePyiachokView.as_view()),
]
