from django.apps import apps as django_apps
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

class Project(models.Model):

  class Meta:
    indexes = [
        models.Index(fields=['project_code',]),
    ]
  challenge = models.ForeignKey('app_challenges.Challenge', default=1, on_delete=models.PROTECT)
  project_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True )
  project_name = models.CharField(("Projekt-Titel"), max_length=140, unique=True)
  project_description = models.TextField(("Projektbeschreibung"), max_length=255)

  push_notifications = models.BooleanField(("Push notfications"), default=True)
  project_code = models.CharField(("Project Code"),max_length=7, blank=True, unique=True)
  
  def __str__(self):
    return self.project_name

  def save(self, *args, **kwargs):
    # If Task doesn't already exist create an (empty) ProjectTask for each Project in the database upfront.
    if self.pk is None:

    # Create Project with unique project code
      generated_code = get_random_string(length=7).lower()

      # Check if generated_code already exist in the DB and regenerate if true
      while Project.objects.filter(project_code = generated_code):
        generated_code = get_random_string(length=7).lower()

      self.project_code = generated_code
      super(Project, self).save(*args, **kwargs)

    # Create new ProjectTasks for every Task 

      models_dict = {
        'TaskProblem': 'ProjectTaskProblem',
        'TaskIdea': 'ProjectTaskIdea',
        'TaskAction': 'ProjectTaskAction',
        # 'TaskOpen': 'ProjectTaskOpen',
        # 'TaskYesOrNo': 'ProjectTaskYesOrNo',
        # 'TaskMultiple': 'ProjectTaskMultiple',
      }

      for key_model, value_model in models_dict.items(): 
    
        # challenge_model = django_apps.get_model('app_challenges', 'Challenge')

        tasks_model = django_apps.get_model('app_tasks', key_model)
        project_task_model = django_apps.get_model('app_project_tasks', value_model)

        # challenge_tasks = challenge_model.objects.filter(id = self.challenge.id).first().tasks.all().filter()
        # print(challenge_tasks)
        tasks = tasks_model.objects.all()

        project_task_list = []
        for task in challenge_tasks:
          project_task_list.append(project_task_model(project = self, task = task))
        project_task_model.objects.bulk_create(project_task_list)

    # End
    else:
      super(Project, self).save(*args, **kwargs)
  # COMMENT OUT AT NEW DEPLOY


