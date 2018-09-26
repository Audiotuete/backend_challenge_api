from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class ProjectTask(models.Model):
  project = models.ForeignKey('app_projects.Project', default=1, on_delete=models.CASCADE)
  submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
  first_touched = models.DateTimeField(null=True, blank=True)
  last_touched = models.DateTimeField(auto_now=True)
  count_touched = models.PositiveIntegerField(default=0)
  status = models.BooleanField(default=False)

  class Meta:
    abstract = True
    unique_together = ['project', 'task']

  def __str__(self):
    return str(self.project)

class ProjectTaskYesOrNo(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskYesOrNo', on_delete=models.CASCADE )
  task_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(0)])
  task_note = models.TextField(max_length=250, null=True, blank=True)

class ProjectTaskOpen(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskOpen', on_delete=models.CASCADE )
  task_text = models.TextField(max_length=250, null=True, blank=True)

class ProjectTaskMultiple(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskMultiple', on_delete=models.CASCADE )
  task_choice_key = models.IntegerField(default=-1, validators=[MinValueValidator(0)])

class ProjectTaskProblem(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskProblem', on_delete=models.CASCADE )
  keywords = models.TextField(max_length=250, null=True, blank=True)
  # description = models.TextField(max_length=150, null=True, blank=True)

class ProjectTaskIdea(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskIdea', on_delete=models.CASCADE )
  # description = models.TextField(max_length=250, null=True, blank=True)
  hashtag_1 = models.CharField(max_length=28, null=True, blank=True)
  hashtag_2 = models.CharField(max_length=28, null=True, blank=True)
  hashtag_3 = models.CharField(max_length=28, null=True, blank=True)

class ProjectTaskAction(ProjectTask):
  task = models.ForeignKey('app_tasks.TaskAction', on_delete=models.CASCADE )
  # description = models.TextField(max_length=250, null=True, blank=True)
  action_1 = models.CharField(max_length=28, null=True, blank=True)
  action_2 = models.CharField(max_length=28, null=True, blank=True)
  action_3 = models.CharField(max_length=28, null=True, blank=True)
 


