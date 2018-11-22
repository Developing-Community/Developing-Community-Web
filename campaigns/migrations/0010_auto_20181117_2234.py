# Generated by Django 2.0.9 on 2018-11-17 22:34

import campaigns.models
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0009_auto_20181116_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, height_field='height_field', null=True, upload_to=campaigns.models.campaign_image_upload_location, width_field='width_field'),
        ),
    ]
