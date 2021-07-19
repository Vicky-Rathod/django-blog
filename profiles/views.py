from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    View
)
from .models import Profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'

class ProfileDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-bio-profile.html'
    model = Profile
    fields = ('description',)

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})

class ProfileImageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-image.html'
    model = Profile
    fields = ('image',)

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})

class ProfileShortDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-short_description.html'
    model = Profile
    fields = ('short_description',)

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})

class ProfileSettingsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/update-profile-setting.html'
    model = Profile
    fields = ('full_name', 'date_of_birth', 'gender')

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})