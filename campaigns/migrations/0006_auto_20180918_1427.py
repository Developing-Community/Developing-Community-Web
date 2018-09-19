# Generated by Django 2.0.7 on 2018-09-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_team'),
        ('campaigns', '0005_auto_20180917_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReportRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='rate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='campaigns.ReportRate'),
        ),
        migrations.AddField(
            model_name='report',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repots', to='campaigns.Task'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='users.Profile'),
        ),
    ]