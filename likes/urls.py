from django.urls import path
from .views import PostLikeView, PostDisLikeView

app_name = 'likes'
urlpatterns = [
    path('like/', PostLikeView.as_view(), name='post_like'),
    path('dislike/', PostDisLikeView.as_view(), name='post_dislike')
]
