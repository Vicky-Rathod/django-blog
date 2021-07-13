from django.urls import path
from .views import (
    ProfileDetailView,
)

app_name = 'profiles'
urlpatterns = [
    path('profile/<str:pk>/', ProfileDetailView.as_view(), name='profile_view'),
]
