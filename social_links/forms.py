from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from accounts.models import Account
from .models import SocialLink

SocailLinkModelForm = inlineformset_factory(Account, SocialLink, fields=('social_name', 'social_link'), extra=1)