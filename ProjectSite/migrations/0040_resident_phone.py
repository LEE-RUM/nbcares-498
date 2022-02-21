# Generated by Django 3.2.8 on 2022-02-21 21:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0039_auto_20220221_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
