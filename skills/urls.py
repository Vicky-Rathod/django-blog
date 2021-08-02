from django.urls import path
from .views import SkillEditView

app_name = 'skills'

urlpatterns = [
    path('update/<str:pk>/', SkillEditView.as_view(), name='update_skill_view')
]
