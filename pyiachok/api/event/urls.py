from django.urls import path
from .views import CreatePyiachokView, ShowPyiachokView

urlpatterns = [
    path('place/<int:pk>/create_event/', CreatePyiachokView.as_view()),
    path('place/<int:pk>/event/<int:sk>/', ShowPyiachokView.as_view()),
]
