# Generated by Django 3.2.8 on 2022-02-14 22:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0026_blog_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=True, null=True),
        ),
    ]
