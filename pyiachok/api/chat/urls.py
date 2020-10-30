from django.urls import path

from .views import CreateMessageView, ShowMessagesView, EditMessageView

urlpatterns = [
    path('event/<int:sk>/add-message/', CreateMessageView.as_view()),
    path('event/<int:sk>/show-messages/', ShowMessagesView.as_view()),
    path('chat-messages/<int:msg_id>/edit', EditMessageView.as_view()),
]
