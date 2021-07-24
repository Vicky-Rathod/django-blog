# Generated by Django 3.2.4 on 2021-07-24 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], default='Draft', max_length=12, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('favorites', models.ManyToManyField(blank=True, default=None, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('hashtags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
