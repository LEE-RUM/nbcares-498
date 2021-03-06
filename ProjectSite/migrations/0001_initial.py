# Generated by Django 3.2.8 on 2022-02-02 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(choices=[('After-school', 'After-school'), ('Art', 'Art'), ('Babysitting', 'Babysitting'), ('Baseball', 'Baseball'), ('Culinary', 'Culinary'), ('Dance', 'Dance'), ('Engineering', 'Engineering'), ('Fashion', 'Fashion'), ('Football', 'Football'), ('Gardening & Nutrition', 'Gardening & Nutrition'), ('Gymnastics', 'Gymnastics'), ('Karate', 'Karate'), ('Leadership', 'Leadership'), ('Literacy', 'Literacy'), ('Music', 'Music'), ('Nature', 'Nature'), ('Science and Engineering', 'Science and Engineering'), ('Soccer', 'Soccer'), ('Softball', 'Softball'), ('Sports', 'Sports'), ('Theatre', 'Theatre'), ('Wrestling', 'Wrestling'), ('Summer Camp/Activities', 'Summer Camp/Activities'), ('Summer Employment', 'Summer Employment'), ('Adult Mental Health', 'Adult Mental Health'), ('Adult Residential', 'Adult Residential'), ('Alternative Education', 'Alternative Education'), ('Behavioral Health', 'Behavioral Health'), ('Case Management', 'Case Management'), ("Children's Outpatient", "Children's Outpatient"), ("Children's Group Care", "Children's Group Care"), ("Children's Intensive", "Children's Intensive"), ('Family Services', 'Family Services'), ('Parenting Groups', 'Parenting Groups'), ('Substance Abuse', 'Substance Abuse'), ('Autism', 'Autism'), ('Childcare & Preschool', 'Childcare & Preschool'), ('College Readiness', 'College Readiness'), ('Community Engagement', 'Community Engagement'), ('People with Disabilities', 'People with Disabilities'), ('Domestic Violence', 'Domestic Violence'), ('Educational Advocacy', 'Educational Advocacy'), ('Elderly Services', 'Elderly Services'), ('Employment', 'Employment'), ('Employment (Youth)', 'Employment (Youth)'), ('ESL (English 2ndLanguage)', 'ESL (English 2ndLanguage)'), ('Financial Lit. & Assist.', 'Financial Lit. & Assist.'), ('G.E.D Programs', 'G.E.D Programs'), ('Housing', 'Housing'), ('Immigrant Resources', 'Immigrant Resources'), ('Legal Aide', 'Legal Aide'), ('Literacy', 'Literacy'), ('Mentoring', 'Mentoring'), ('Pregnancy Prevention', 'Pregnancy Prevention'), ('Transportation', 'Transportation'), ('Tutoring', 'Tutoring'), ('Veteran Services', 'Veteran Services')], max_length=30, null=True)),
                ('contact_resource_provider', models.CharField(max_length=50)),
                ('contact_ages', models.CharField(max_length=20)),
                ('contact_websites', models.CharField(max_length=40, null=True)),
                ('contact_location', models.CharField(max_length=45)),
                ('contact_number', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, null=True)),
                ('event_description', models.TextField(blank=True, max_length=400, null=True)),
                ('event_sTime', models.DateTimeField()),
                ('event_eTime', models.DateTimeField()),
                ('event_tag', models.CharField(choices=[('Housing', 'Housing'), ('Employment', 'Employment'), ('Education', 'Education'), ('Financial Literacy', 'Financial Literacy'), ('Healthcare', 'Healthcare'), ('Mental Health', 'Mental Health'), ('Family Engagement', 'Family Engagement'), ('Children Activities', 'Children Activities'), ('Art', 'Art'), ('Community Event', 'Community Event'), ('Fundraising', 'Fundraising'), ('Other', 'Other')], max_length=30, null=True)),
                ('event_status', models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Requested For Change', 'Requested For Change')], default='Pending', max_length=30)),
                ('event_date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=40, null=True)),
                ('org_address', models.CharField(blank=True, max_length=60, null=True)),
                ('org_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('org_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('org_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('org_date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_event_status', models.CharField(choices=[('Accepted', 'Accepted'), ('Waiting Approval', 'Waiting Approval')], max_length=20, null=True)),
                ('org_event_date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('org_event_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectSite.event')),
                ('org_event_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectSite.organization')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectSite.organization'),
        ),
    ]
