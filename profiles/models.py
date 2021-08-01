from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
import datetime
from PIL import Image
import os

# Profile images unique path generatore..
def ProfileAvatarUploadPathGenerate(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_avatar_name = 'user_{0}/avatar.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.DEFAULT_FILE_STORAGE, profile_avatar_name)
    if os.path.exists(full_path):
    	os.remove(full_path)
    return profile_avatar_name

class Profile(models.Model):
    CHOICES_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Custom', 'Custom'),
        ('Third gender', 'Third gender')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(_("Full name"), max_length=250)
    short_description = models.CharField(_("Short Description"), default='Wiring for your shirt description', max_length=100)
    description =  models.TextField(_("description"), default='Your your details....')
    image = models.ImageField(_("Image"), upload_to=ProfileAvatarUploadPathGenerate)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    gender = models.CharField(_("Gander"), choices=CHOICES_GENDER, max_length=20)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     SIZE = 250, 250

    #     if self.image:
    #         avatar = Image.open(self.image.path)
    #         avatar.thumbnail(SIZE, Image.LANCZOS)
    #         avatar.save(self.image.path)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile:profile_view", kwargs={"pk": self.pk})
    
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return "https://res.cloudinary.com/mohammadanarul/image/upload/v1627591816/avatar_to8zm9.png"
    
    

