# Generated by Django 2.0.8 on 2018-10-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0004_taskaction'),
        ('app_challenges', '0015_auto_20181017_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='tasks',
            field=models.ManyToManyField(to='app_tasks.Task', verbose_name='Aufgaben'),
        ),
    ]
