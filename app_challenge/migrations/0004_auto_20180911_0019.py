# Generated by Django 2.0.8 on 2018-09-11 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_challenge', '0003_auto_20180911_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmultiple',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='questionopen',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='questionyesorno',
            name='question_type',
        ),
    ]
