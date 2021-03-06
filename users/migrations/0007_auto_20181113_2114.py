# Generated by Django 2.0.9 on 2018-11-13 21:14

import sorl.thumbnail.fields
from django.db import migrations, models

import users.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_auto_20181113_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=sorl.thumbnail.fields.ImageField(blank=True, height_field='height_field', null=True,
                                                   upload_to=users.models.profile_image_upload_location,
                                                   width_field='width_field'),
        ),
    ]
