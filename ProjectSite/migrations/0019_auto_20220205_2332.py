# Generated by Django 3.2.8 on 2022-02-06 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0018_auto_20220205_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='myvideos',
            new_name='video_urls',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='video_url',
        ),
    ]
