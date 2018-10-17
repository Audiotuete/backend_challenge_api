# Generated by Django 2.0.8 on 2018-10-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_challenges', '0010_auto_20181017_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengedates',
            name='event_time',
        ),
        migrations.AddField(
            model_name='challengedates',
            name='event_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Uhrzeit - Ende'),
        ),
        migrations.AddField(
            model_name='challengedates',
            name='event_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Uhrzeit - Beginn'),
        ),
    ]
