from django.urls import path
from .views import (
    LogoutView,
    UserLoginView,
    UserRegisterView,
    PasswordResetRequestView,
    UserAccountActivateView,
)

app_name = 'Account'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('login/', UserLoginView.as_view(), name='login_view'),
    path('register/', UserRegisterView.as_view(), name='user_register_view'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_view'),
    path('activate/<uid>/<token>', UserAccountActivateView.as_view(), name='activate_view'),
]