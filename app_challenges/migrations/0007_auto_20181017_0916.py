# Generated by Django 2.0.8 on 2018-10-17 09:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_challenges', '0006_auto_20180922_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Veranstaltung')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='Datum')),
                ('event_time', models.TimeField(blank=True, null=True, verbose_name='Uhrzeit')),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='contact_info',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
