# Generated by Django 3.2.8 on 2022-02-06 04:14

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0009_alter_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', embed_video.fields.EmbedVideoField(blank=True, null=True)),
            ],
        ),
    ]
