# Generated by Django 3.2.8 on 2022-02-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0019_auto_20220205_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='image', max_length=128)),
                ('img', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ManyToManyField(blank=True, to='ProjectSite.Images'),
        ),
    ]
