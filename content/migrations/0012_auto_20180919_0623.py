# Generated by Django 2.0.7 on 2018-09-19 06:23

import content.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20180919_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='main_type',
            field=enumfields.fields.EnumField(default='TEXT', enum=content.models.MainContentType, max_length=1),
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=enumfields.fields.EnumField(default='ARTICLE', enum=content.models.ContentType, max_length=1),
        ),
        migrations.AddField(
            model_name='content',
            name='visibility',
            field=enumfields.fields.EnumField(default='PUBLIC', enum=content.models.ContentVisibility, max_length=1),
        ),
        migrations.AddField(
            model_name='contentrelation',
            name='type',
            field=enumfields.fields.EnumField(default='COMMENTED_ON', enum=content.models.ContentRealtionType, max_length=1),
        ),
    ]