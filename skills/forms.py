from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from accounts.models import Account
from .models import Skill

SkillFormset = inlineformset_factory(Account, Skill, fields=('name',), extra=1)