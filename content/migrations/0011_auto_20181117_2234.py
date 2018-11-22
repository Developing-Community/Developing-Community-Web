# Generated by Django 2.0.9 on 2018-11-17 22:34

import content.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20181116_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=enumfields.fields.EnumField(blank=True, default='article', enum=content.models.ContentType, max_length=1000),
        ),
    ]
