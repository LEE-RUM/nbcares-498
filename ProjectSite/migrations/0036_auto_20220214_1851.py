# Generated by Django 3.2.8 on 2022-02-14 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0035_auto_20220214_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='video_urls',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
