from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=250)
    description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Create time"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Update time"), auto_now=True, auto_now_add=False)