from django.urls import path
from .views import (
    ProfileView,
    ProfileDescriptionUpdateView,
    ProfileImageUpdateView,
    ProfileShortDescriptionUpdateView,
    ProfileSettingsUpdateView
)

app_name = 'profiles'
urlpatterns = [
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile_view'),
    path('u/<str:pk>/', ProfileDescriptionUpdateView.as_view(), name='update_profile_description_view'),
    path('image-update/<str:pk>/', ProfileImageUpdateView.as_view(), name='update_profile_image'),
    path('short-description-update/<str:pk>/', ProfileShortDescriptionUpdateView.as_view(), name='short_description_update'),
    path('profile-settings-update/<str:pk>/', ProfileSettingsUpdateView.as_view(), name='profile_settings_update'),
]
