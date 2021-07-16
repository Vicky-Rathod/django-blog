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

class ProfileDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-bio-profile.html'
    model = Profile
    fields = ('bio',)
    success_url = '/'

class ProfileImageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-image.html'
    model = Profile
    fields = ('image',)
    success_url = '/'

class ProfileShortDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-short_description.html'
    model = Profile
    fields = ('short_description',)
    success_url = '/'

class ProfileSettingsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-profile-setting.html'
    model = Profile
    fields = ('full_name', 'date_of_birth', 'gender')
    success_url = '/'