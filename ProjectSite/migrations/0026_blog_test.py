# Generated by Django 3.2.8 on 2022-02-14 22:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0025_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=True, null=True),
        ),
    ]