# Generated by Django 2.0.7 on 2018-09-21 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import users.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('companions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('complete_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, height_field='height_field', null=True,
                                                    upload_to=users.models.profile_image_upload_location,
                                                    width_field='width_field')),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('subscribe_to_newsletter', models.BooleanField(default=True)),
                ('email_publicity', models.BooleanField(default=True)),
                ('applications', models.ManyToManyField(blank=True, to='companions.Application')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info',
                                       to='users.Profile'),
        ),
    ]
