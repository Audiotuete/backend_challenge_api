# Generated by Django 2.0.8 on 2018-09-22 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0005_auto_20180922_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(max_length=255, verbose_name='Projektbeschreibung'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=140, verbose_name='Projekt-Titel'),
        ),
    ]