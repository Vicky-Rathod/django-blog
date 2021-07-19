from django.urls import path
from .views import (
    CommentCreateView,
)

app_name = 'comments'
urlpatterns = [
    path('add-comment/<slug>/', CommentCreateView.as_view(), name='add_comment_view'),
]
