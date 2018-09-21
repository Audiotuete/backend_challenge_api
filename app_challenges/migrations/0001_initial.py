# Generated by Django 2.0.8 on 2018-09-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(blank=True, max_length=150, verbose_name='Kontext (Schule- / Kommune)')),
                ('city', models.CharField(blank=True, max_length=150, verbose_name='Stadt')),
                ('year', models.IntegerField(choices=[(2018, 2018), (2019, 2019)], default=2018, verbose_name='Jahr')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start-Datum')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End-Datum')),
                ('challenge_code', models.CharField(blank=True, max_length=7, null=True, unique=True, verbose_name='Challenge Code')),
            ],
        ),
    ]
