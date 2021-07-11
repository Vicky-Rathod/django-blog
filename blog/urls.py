from django.urls import path
from .views import (
    HomeView,
    AddPostView,
)

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('add-post/', AddPostView.as_view(), name='add_post_view'),
]
