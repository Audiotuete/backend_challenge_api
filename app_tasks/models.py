from django.apps import apps as django_apps
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from ordered_model.models import OrderedModel


class Question(OrderedModel):
  # poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
  task_text = models.TextField(max_length=250)
  task_videolink = models.CharField(max_length=150, null=True, blank=True)
  task_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  order_class_path = __module__ + '.Question'
  # position = PositionField(collection='poll', parent_link='task_ptr')

  class Meta:
    ordering = ('order',)
    # abstract = True

  def __str__(self):
    return self.task_text

  def save(self, *args, **kwargs):
    Project = django_apps.get_model('app_projects', 'Project')
    # If User doesn't already exist create an (empty) UserAnswer entry for each Question in the database upfront.
    if self.pk is None:
      super(Question, self).save(*args, **kwargs)
      
      all_projects = Project.objects.all()
      project_task_list = []
      # for a_project in all_projects:
      #     project_task_list.append(UserAnswer(project = a_project, task = self))

      # UserAnswer.objects.bulk_create(project_task_list)     

      subclass_name = self.__class__.__name__
      
      if subclass_name == 'QuestionYesOrNo':
        for a_project in all_projects:
          project_task_list.append(UserAnswerYesOrNo(project = a_project, task = self))

        UserAnswerYesOrNo.objects.bulk_create(project_task_list)

      elif subclass_name == 'QuestionOpen':
        for a_project in all_projects:
  
          project_task_list.append(UserAnswerOpen(project = a_project, task = self))

        UserAnswerOpen.objects.bulk_create(project_task_list)

      elif subclass_name == 'QuestionMultiple':
        for a_project in all_projects:
          project_task_list.append(UserAnswerMultiple(project = a_project, task = self))

        UserAnswerMultiple.objects.bulk_create(project_task_list)
      else:
          pass
    # End
    else:
      super(Question, self).save(*args, **kwargs)

class QuestionYesOrNo(Question):
  pass

class QuestionOpen(Question):
  pass

class QuestionMultiple(Question):
  options = ArrayField(models.CharField(max_length=150, blank=True), default=list, null=True, size=4)

class UserAnswer(models.Model):
  project = models.ForeignKey('app_projects.Project', default=0, on_delete=models.CASCADE)
  first_touched = models.DateTimeField(null=True, blank=True)
  last_touched = models.DateTimeField(auto_now=True)
  count_touched = models.PositiveIntegerField(default=0)

  class Meta:
    abstract = True
    unique_together = ['project', 'task']

  def __str__(self):
    return str(self.project)

class UserAnswerYesOrNo(UserAnswer):
  task = models.ForeignKey('QuestionYesOrNo', on_delete=models.CASCADE )
  answer_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(0)])
  answer_note = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerOpen(UserAnswer):
  task = models.ForeignKey('QuestionOpen', on_delete=models.CASCADE )
  answer_text = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerMultiple(UserAnswer):
  task = models.ForeignKey('QuestionMultiple', on_delete=models.CASCADE )
  answer_choice_key = models.IntegerField(default=-1, validators=[MinValueValidator(0)])
  # option_set = models.ForeignKey('OptionSet', on_delete=models.CASCADE, default=1 )
  # option = models.ForeignKey('Option', on_delete=models.CASCADE )

# class OptionSet(models.Model):
#   set_name = models.CharField(max_length=150, null=True, blank=True)

#   def __str__(self):
#     return str(self.set_name)





 


