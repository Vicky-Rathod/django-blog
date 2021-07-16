from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL
class Skill(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=150)
