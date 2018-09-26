# Generated by Django 2.0.8 on 2018-09-24 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0007_auto_20180922_1308'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_tasks', '0003_taskidea'),
        ('app_project_tasks', '0002_auto_20180924_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTaskIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('hashtag_1', models.CharField(blank=True, max_length=28, null=True)),
                ('hashtag_2', models.CharField(blank=True, max_length=28, null=True)),
                ('hashtag_3', models.CharField(blank=True, max_length=28, null=True)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_projects.Project')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tasks.TaskIdea')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='projecttaskidea',
            unique_together={('project', 'task')},
        ),
    ]
