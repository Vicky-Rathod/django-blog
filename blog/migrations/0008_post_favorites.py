# Generated by Django 3.2.5 on 2021-07-18 22:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
