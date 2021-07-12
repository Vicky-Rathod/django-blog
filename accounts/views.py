from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
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
    def get(self, *args, **kwargs):
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
                    return HttpResponse("<a href='/'>Inactive User</a>")
            else:
                return HttpResponse("<a href='/'>Inactive User</a>")
                
class UserRegisterView(View):
    template_name = 'account/register.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
    def post(self, request, *args, **kwargs):
        form = AccountRegisterForm()
        if request.method == 'POST':
            form = AccountRegisterForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.is_active = False
                instance.save()
                site = get_current_site(request)
                mail_subject = 'Activate your account.'
                email_template_name = 'account/email-confirm.html'
                messages = render_to_string(email_template_name,{
                    'user': instance,
                    'domain': site.domain,
                    'uid': instance.id,
                    'token': UserAccountRegisterActiveTokenGenerate.make_token(instance)
                })
                to_mail = form.cleaned_data.get('email')
                to_list = [to_mail]
                from_email = settings.EMAIL_HOST_USER
                send_mail(mail_subject, messages, from_email, to_list, fail_silently=True)
                return HttpResponse('<h1>Thanks for your registration. A confirmation link was sent to your email.</h1>')

class UserAccountActivateView(View):
    def get(self, request, uid, token):
        try:
            user = get_object_or_404(Account, pk=uid)
        except:
            raise Http404('User is not valide')

        if user is not None and UserAccountRegisterActiveTokenGenerate.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("<h1>Your Blog account activated. Now you can <a href='{% url 'account:login' %}'>login</a></h1>")
        else:
            return HttpResponse('<h1>Your Activation link is Not invalid.</h1>')

class PasswordResetRequestView(View):
    password_reset_form = PasswordResetForm
    template_name = "password_reset/password_reset.html"
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {"password_reset_form": self.password_reset_form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = Account.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "password_reset/password_reset_email.html"
                        site = get_current_site(request)
                        c = {
                            "email":user.email,
                            'domain': site.domain, 
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        from_email = settings.EMAIL_HOST_USER
                        try:
                            send_mail(subject, email, from_email , [user.email], fail_silently=False)
                            return redirect('/')
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                            return redirect ("/password_reset/done/")