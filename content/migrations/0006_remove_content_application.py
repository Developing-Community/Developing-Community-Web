# Generated by Django 2.0.7 on 2018-09-17 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_content_read_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='application',
        ),
    ]
