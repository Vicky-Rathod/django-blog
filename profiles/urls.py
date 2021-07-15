from django.urls import path
from .views import (
    ProfileDetailView,
    ProfileCreateView
)

app_name = 'profiles'
urlpatterns = [
    path('profile/<str:pk>/', ProfileDetailView.as_view(), name='profile_view'),
    path('add/?<str:pk>/', ProfileCreateView.as_view(), name='add_profile_view'),
]
