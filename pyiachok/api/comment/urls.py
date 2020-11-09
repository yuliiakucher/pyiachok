from django.urls import path
from .views import CreateCommentView, ShowCommentsView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('place/<int:pk>/add-comment/', CreateCommentView.as_view()),
    path('place/<int:pk>/show-comments/', ShowCommentsView.as_view()),
    path('comment/<int:comment_id>/edit/', EditCommentView.as_view()),
    path('comment/<int:comment_id>/delete/', DeleteCommentView.as_view()),
]
