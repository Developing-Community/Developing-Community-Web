# Generated by Django 2.0.7 on 2018-09-19 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_campaignenrollmentrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='application',
        ),
    ]
