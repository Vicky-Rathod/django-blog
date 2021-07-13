from django.db import models
from django.conf import settings

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Profile"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=150)
