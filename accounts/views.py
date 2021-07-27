from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View, CreateView
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .tokens import UserAccountRegisterActiveTokenGenerate
from .forms import AccountRegisterForm
from .models import Account

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('blog:home_view')

class UserLoginView(View):
    template_name = 'account/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        return render(self.request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    next = request.META['HTTP_REFERER']
                    return HttpResponseRedirect(next)
            else:
                next = request.META['HTTP_REFERER']
                return HttpResponseRedirect(next)
                
class UserRegisterView(CreateView):
    template_name = 'account/register.html'
    form_class = AccountRegisterForm

    def form_valid(self, form):
        validation=super(UserRegisterView, self).form_valid(form)

        username=form.cleaned_data['username']
        password=form.cleaned_data['password2']
        user=authenticate(self.request, username=username, password=password)
        login(self.request, user)

        return validation