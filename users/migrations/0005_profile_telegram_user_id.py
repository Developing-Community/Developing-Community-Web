# Generated by Django 2.0.7 on 2018-10-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_telegramtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telegram_user_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]