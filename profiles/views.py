from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    View
)
from .models import Profile
from .forms import ProfileForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add-profile.html'
    form_class = ProfileForm