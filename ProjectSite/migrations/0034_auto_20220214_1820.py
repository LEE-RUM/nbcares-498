# Generated by Django 3.2.8 on 2022-02-14 23:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0033_auto_20220214_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='test',
        ),
        migrations.AddField(
            model_name='blog',
            name='test3',
            field=ckeditor.fields.RichTextField(default=True, null=True),
        ),
    ]