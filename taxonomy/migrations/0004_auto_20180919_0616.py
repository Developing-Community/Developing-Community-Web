# Generated by Django 2.0.7 on 2018-09-19 06:16

from django.db import migrations
import enumfields.fields
import taxonomy.models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_auto_20180919_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='taxonomy_type',
            field=enumfields.fields.EnumField(default='subject', enum=taxonomy.models.TaxonomyType, max_length=100),
        ),
        migrations.AddField(
            model_name='termrelation',
            name='type',
            field=enumfields.fields.EnumField(default='child_of', enum=taxonomy.models.TermRealtionType, max_length=100),
        ),
    ]
