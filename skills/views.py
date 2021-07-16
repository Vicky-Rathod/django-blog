from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.contrib import messages                     
from accounts.models import Account
from .models import Skill
from .forms import SkillFormset

class SkillEditView(SingleObjectMixin, FormView):
    template_name = 'edit-skill.html'
    model = Account
    # success_url = '/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Account.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Account.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return SkillFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile:profile_view', kwargs={'pk': self.object.pk})
