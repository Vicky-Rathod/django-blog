from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Skill


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    template_name = 'skill.html'
    fields = ['name']
    success_url = '/'
