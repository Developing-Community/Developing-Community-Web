# Generated by Django 2.0.7 on 2018-09-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20180917_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='height_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='width_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
