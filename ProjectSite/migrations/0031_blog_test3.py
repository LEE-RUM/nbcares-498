# Generated by Django 3.2.8 on 2022-02-14 23:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0030_remove_blog_test2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test3',
            field=ckeditor.fields.RichTextField(default=True, null=True),
        ),
    ]
