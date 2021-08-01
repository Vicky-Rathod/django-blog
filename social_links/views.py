from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from accounts.models import Account
from django.contrib import messages
from django.urls import reverse  
from .models import SocialLink
from .forms import SocailLinkModelForm

class SocialLinkCreateView(SingleObjectMixin, FormView):
    model = Account
    template_name = 'update-social-link.html'
    # success_url = '/'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Account.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Account.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return SocailLinkModelForm(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.info(
            self.request,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})