from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
class SocialLink(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Profile"), on_delete=models.CASCADE)
    social_name = models.CharField(_("social name"), max_length=100)
    social_link = models.CharField(_("Social Link"), max_length=350)