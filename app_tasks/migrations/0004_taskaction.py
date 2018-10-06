# Generated by Django 2.0.8 on 2018-09-24 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0003_taskidea'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAction',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_tasks.Task')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=('app_tasks.task',),
        ),
    ]