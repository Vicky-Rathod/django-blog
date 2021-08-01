from django.urls import path
from .views import (
    LogoutView,
    UserLoginView,
    UserRegisterView,
    UserAccountActivateView,
    password_reset_request_view,
    UserAccountActivateView,
    UserNameChangeCreateView
)

app_name = 'Account'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('login/', UserLoginView.as_view(), name='login_view'),
    path('register/', UserRegisterView.as_view(), name='user_register_view'),
    path('password-reset/', password_reset_request_view, name='password_reset_view'),
    path('activate/<uid>/<token>', UserAccountActivateView.as_view(), name='activate_view'),
    path('username-change/<str:pk>/', UserNameChangeCreateView.as_view(), name='username_change_view')
]