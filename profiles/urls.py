from django.urls import path
from .views import (
    ProfileView,
    ProfileDescriptionUpdateView,
    ProfileImageUpdateView,
    ProfileShortDescriptionUpdateView,
    ProfileInfoUpdateView,
    ProfileSettingView,
)

app_name = 'profiles'
urlpatterns = [
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile_view'),
    path('u/<str:pk>/', ProfileDescriptionUpdateView.as_view(), name='update_profile_description_view'),
    path('image-update/<str:pk>/', ProfileImageUpdateView.as_view(), name='update_profile_image'),
    path('short-description-update/<str:pk>/', ProfileShortDescriptionUpdateView.as_view(), name='short_description_update'),
    path('profile-setting/<str:pk>/', ProfileSettingView.as_view(), name='profile_setting_view'),
    path('profile-info-update/<str:pk>/', ProfileInfoUpdateView.as_view(), name='profile_info_update'),
]
