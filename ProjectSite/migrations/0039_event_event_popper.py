# Generated by Django 4.0.2 on 2022-02-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0038_remove_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_popper',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
