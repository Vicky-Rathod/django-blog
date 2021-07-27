from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Post
from .utils import random_string_generator

@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = random_string_generator(size=50)
        instance.save()