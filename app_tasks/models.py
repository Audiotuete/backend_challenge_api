from django.apps import apps as django_apps
from django.db import models
from django.contrib.postgres.fields import ArrayField
from ordered_model.models import OrderedModel


class Task(OrderedModel):
  # poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
  task_text = models.TextField(max_length=250)
  task_videolink = models.CharField(max_length=150, null=True, blank=True)
  task_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  order_class_path = __module__ + '.Task'
  # position = PositionField(collection='poll', parent_link='task_ptr')

  class Meta:
    ordering = ('order',)
    # abstract = True

  def __str__(self):
    return self.task_text

  def save(self, *args, **kwargs):
    Project = django_apps.get_model('app_projects', 'Project')
    # If User doesn't already exist create an (empty) ProjectTask entry for each Task in the database upfront.
    if self.pk is None:
      super(Task, self).save(*args, **kwargs)
      
      all_projects = Project.objects.all()
      project_task_list = []
      # for a_project in all_projects:
      #     project_task_list.append(ProjectTask(project = a_project, task = self))

      # ProjectTask.objects.bulk_create(project_task_list)     

      subclass_name = self.__class__.__name__
      
      if subclass_name == 'TaskYesOrNo':
        for a_project in all_projects:
          project_task_list.append(ProjectTaskYesOrNo(project = a_project, task = self))

        ProjectTaskYesOrNo.objects.bulk_create(project_task_list)

      elif subclass_name == 'TaskOpen':
        for a_project in all_projects:
  
          project_task_list.append(ProjectTaskOpen(project = a_project, task = self))

        ProjectTaskOpen.objects.bulk_create(project_task_list)

      elif subclass_name == 'TaskMultiple':
        for a_project in all_projects:
          project_task_list.append(ProjectTaskMultiple(project = a_project, task = self))

        ProjectTaskMultiple.objects.bulk_create(project_task_list)
      else:
          pass
    # End
    else:
      super(Task, self).save(*args, **kwargs)

class TaskYesOrNo(Task):
  pass

class TaskOpen(Task):
  pass

class TaskMultiple(Task):
  options = ArrayField(models.CharField(max_length=150, blank=True), default=list, null=True, size=4)




 


