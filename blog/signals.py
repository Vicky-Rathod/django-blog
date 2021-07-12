from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Post
from .utils import unique_slug_generator

@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

@receiver(pre_save, sender=Post)
def save_user_profile(sender, instance, **kwargs):
   instance.slug = unique_slug_generator(instance)