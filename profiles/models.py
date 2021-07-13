from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import datetime
class Profile(models.Model):
    CHOICES_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Custom', 'Custom'),
        ('Third gender', 'Third gender')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(_("Full name"), max_length=250)
    short_description = models.CharField(_("Short Description"), max_length=300)
    bio =  models.TextField(_("Bio"))
    image = models.ImageField(_("Image"), upload_to=None)
    date_of_birth = models.DateTimeField(_("Date of birth"), blank=True, null=True)
    gender = models.CharField(_("Gander"), choices=CHOICES_GENDER, max_length=20)

