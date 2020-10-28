from django.urls import path
from .views import CreateMessageView, ShowMessagesView

urlpatterns = [
    path('place/<int:pk>/event/<int:sk>/add_msg/', CreateMessageView.as_view()),
    path('place/<int:pk>/event/<int:sk>/show_msgs/', ShowMessagesView.as_view()),
]
