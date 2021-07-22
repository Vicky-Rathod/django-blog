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
from blog.models import Post
from .models import Profile

class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile/profile.html'
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        post = Post.objects.filter(user=request.user)
        return render(request, self.template_name, {'object': profile, 'post': post})

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