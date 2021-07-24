from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# from profiles.models import Profile

User = settings.AUTH_USER_MODEL
SOCIAL_NAME = (
    ('Facebook', 'fa-facebook-square'),
    ('LinkedIn', 'fa-linkedin'),
    ('Twitter', 'fa-twitter-square'),
    ('YouTube', 'fa-youtube'),
    ('Pinterest', 'fa-pinterest-square'),
    ('Instagram', 'fa-instagram'),
    ('Reddit', 'fa-reddit'),
    ('Quora', 'fa-quora'),
    ('WhatsApp', 'fa-whatsapp'),
    ('Medium', 'fa-medium'),
    ('TikTok', 'fa-tiktok'),
)
class SocialLink(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Profile"), on_delete=models.CASCADE)
    social_name = models.CharField(_("social name"), max_length=20, choices=SOCIAL_NAME)
    social_link = models.CharField(_("Social Link"), max_length=350)