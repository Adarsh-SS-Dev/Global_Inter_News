# Generated by Django 4.1.4 on 2023-08-03 17:02

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('home', '0007_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='group',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
