from django.urls import path
from .views import SkillCreateView

app_name = 'skills'
urlpatterns = [
    path('add/', SkillCreateView.as_view(), name='add_update_skill_view')
]
