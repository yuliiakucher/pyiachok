from django.urls import path
from .views import CreateCommentView,ShowCommentsView

urlpatterns = [
    path('place/<int:pk>/add_comment/', CreateCommentView.as_view()),
    path('place/<int:pk>/show_comments/', ShowCommentsView.as_view()),
]
