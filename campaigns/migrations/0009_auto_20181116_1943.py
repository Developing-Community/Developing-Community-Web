# Generated by Django 2.0.9 on 2018-11-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_auto_20181109_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='campaign',
            unique_together={('slug', 'type')},
        ),
    ]