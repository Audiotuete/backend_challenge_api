# Generated by Django 2.0.8 on 2018-09-25 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_project_tasks', '0004_auto_20180924_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttaskaction',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projecttaskidea',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projecttaskproblem',
            name='description',
        ),
    ]
