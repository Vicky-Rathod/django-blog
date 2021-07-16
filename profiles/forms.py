from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name','short_description', 'bio', 'image', 'date_of_birth', 'gender')