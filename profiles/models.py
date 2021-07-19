from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import datetime

def ProfileAvatarUploadPathGenerate(instance, filename):
    return 'profile/users/avatar/{0}/{1}'.format(instance.user.id, filename)
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
    description =  models.TextField(_("description"), default='Your your details....')
    image = models.ImageField(_("Image"), upload_to=ProfileAvatarUploadPathGenerate, default='profile/avatar.png')
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    gender = models.CharField(_("Gander"), choices=CHOICES_GENDER, max_length=20)

    def __str__(self):
        return self.user.username
    

