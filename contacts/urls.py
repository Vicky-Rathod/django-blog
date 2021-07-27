from django.urls import path
from .views import ContactFormView

app_name = 'contacts'
urlpatterns = [
    path('c/', ContactFormView.as_view(), name='contact_view'),
]
