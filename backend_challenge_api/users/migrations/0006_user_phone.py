# Generated by Django 2.0.8 on 2018-10-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180925_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefon-Nummer'),
        ),
    ]
