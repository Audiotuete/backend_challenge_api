# Generated by Django 2.0.8 on 2018-09-25 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180923_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currentChallenge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_challenges.Challenge'),
        ),
    ]
