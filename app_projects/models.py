from django.db import models

from app_tasks.models import TaskOpen, TaskYesOrNo, TaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple


class Project(models.Model):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  project_name = models.CharField(("Projectname"), blank=True, max_length=255)

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  push_notifications = models.BooleanField(("Push notfications enabled"), default=True)
  reg_code = models.CharField(("Registration Code"),max_length=8, null=True, blank=True)
  # COMMENT OUT AT NEW DEPLOY
  
  def __str__(self):
    return self.project_name

  # COMMENT OUT AT NEW DEPLOY
  def save(self, *args, **kwargs):
    # If Task doesn't already exist create an (empty) ProjectTask entry for each Project in the database upfront.
    if self.pk is None:

      super(Project, self).save(*args, **kwargs)
      
      open_tasks = TaskOpen.objects.all()
      multiple_choice_tasks = TaskMultiple.objects.all()
      yes_or_no_tasks = TaskYesOrNo.objects.all()

      project_task_list = []
 
      for new_task in open_tasks:
        project_task_list.append(ProjectTaskOpen(project = self, task = new_task))
      ProjectTaskOpen.objects.bulk_create(project_task_list)

      project_task_list = []
 
      for new_task in multiple_choice_tasks:
        project_task_list.append(ProjectTaskMultiple(project = self, task = new_task))
      ProjectTaskMultiple.objects.bulk_create(project_task_list)
      
      project_task_list = []  

      for new_task in yes_or_no_tasks:
        project_task_list.append(ProjectTaskYesOrNo(project = self, task = new_task))
      
      ProjectTaskYesOrNo.objects.bulk_create(project_task_list)
      project_task_list = []  

    # End
    else:
      super(Project, self).save(*args, **kwargs)
  # COMMENT OUT AT NEW DEPLOY

