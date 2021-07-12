from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is alredy used.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            username = Account.object.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Username {username} is alredy used')