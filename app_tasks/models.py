from django.apps import apps as django_apps
from django.db import models
from django.contrib.postgres.fields import ArrayField
from ordered_model.models import OrderedModel

class Task(OrderedModel):
  task_text = models.TextField(max_length=250)
  task_videolink = models.CharField(max_length=150, null=True, blank=True)
  task_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  order_class_path = __module__ + '.Task'

  class Meta:
    ordering = ('order',)

  def __str__(self):
    return self.task_text

  def save(self, *args, **kwargs):
    Project = django_apps.get_model('app_projects', 'Project')
    # If Project doesn't already exist create an (empty) ProjectTask for each Task in the database upfront.
    if self.pk is None:
      super(Task, self).save(*args, **kwargs)
            
      all_models = {
        'TaskProblem': 'ProjectTaskProblem',
        'TaskIdea': 'ProjectTaskIdea',
        'TaskAction': 'ProjectTaskAction',
        # 'TaskOpen': 'ProjectTaskOpen',
        # 'TaskYesOrNo': 'ProjectTaskYesOrNo',
        # 'TaskMultiple': 'ProjectTaskMultiple',
      }

      task_model_name = self.__class__.__name__
      project_task_model = django_apps.get_model('app_project_tasks', model_dict[task_model_name])

      all_projects = Project.objects.all()

      projecttask_list = []    
      for a_project in all_projects:
        projecttask_list.append(project_task_model(project = a_project, task = self))

      project_task_model.objects.bulk_create(projecttask_list)

    else:
      super(Task, self).save(*args, **kwargs)


class TaskProblem(Task):
  pass

class TaskIdea(Task):
  pass

class TaskAction(Task):
  pass

class TaskYesOrNo(Task):
  pass

class TaskOpen(Task):
  pass

class TaskMultiple(Task):
  options = ArrayField(models.CharField(max_length=150, blank=True), default=list, null=True, size=4)

 


