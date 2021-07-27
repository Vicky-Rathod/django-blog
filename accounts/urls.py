from django.urls import path
from .views import (
    LogoutView,
    UserLoginView,
    UserRegisterView,
)

app_name = 'Account'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('login/', UserLoginView.as_view(), name='login_view'),
    path('register/', UserRegisterView.as_view(), name='user_register_view'),
]