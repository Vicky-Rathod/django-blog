# Generated by Django 3.2.5 on 2021-07-23 17:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]