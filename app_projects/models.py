from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

from app_tasks.models import TaskOpen, TaskYesOrNo, TaskMultiple
from app_project_tasks.models import ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple



class Project(models.Model):

  class Meta:
    indexes = [
        models.Index(fields=['project_code',]),
    ]

  # First Name and Last Name do not cover name patterns
  # around the globe.

  challenge = models.ForeignKey('app_challenges.Challenge', default=1, on_delete=models.PROTECT)
  project_creator = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT)
  project_name = models.CharField(("Projekt-Titel"), blank=True, max_length=140)
  project_description = models.TextField(("Projektbeschreibung"), blank=True, max_length=255)

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  push_notifications = models.BooleanField(("Push notfications"), default=True)
  project_code = models.CharField(("Project Code"),max_length=7, blank=True, unique=True)


  # COMMENT OUT AT NEW DEPLOY
  
  def __str__(self):
    return self.project_name

  # COMMENT OUT AT NEW DEPLOY
  def save(self, *args, **kwargs):
    # If Task doesn't already exist create an (empty) ProjectTask entry for each Project in the database upfront.
    if self.pk is None:

      generated_code = get_random_string(length=7).lower()

      while Project.objects.filter(project_code = generated_code):
        generated_code = get_random_string(length=7).lower()

      self.project_code = generated_code

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


