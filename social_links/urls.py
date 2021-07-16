from django.urls import path
from .views import (
    SocialLinkCreateView,
)

app_name = 'social_links'
urlpatterns = [
    path('update/<str:pk>/', SocialLinkCreateView.as_view(), name='update_social_link_view'),
]
