from django.db import models

from app_tasks.models import QuestionOpen, QuestionYesOrNo, QuestionMultiple, UserAnswerOpen, UserAnswerYesOrNo, UserAnswerMultiple


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
    # If Question doesn't already exist create an (empty) UserAnswer entry for each Project in the database upfront.
    if self.pk is None:

      super(Project, self).save(*args, **kwargs)
      
      open_questions = QuestionOpen.objects.all()
      multiple_choice_questions = QuestionMultiple.objects.all()
      yes_or_no_questions = QuestionYesOrNo.objects.all()

      project_task_list = []
 
      for new_question in open_questions:
        project_task_list.append(UserAnswerOpen(project = self, question = new_question))
      UserAnswerOpen.objects.bulk_create(project_task_list)

      project_task_list = []
 
      for new_question in multiple_choice_questions:
        project_task_list.append(UserAnswerMultiple(project = self, question = new_question))
      UserAnswerMultiple.objects.bulk_create(project_task_list)
      
      project_task_list = []  

      for new_question in yes_or_no_questions:
        project_task_list.append(UserAnswerYesOrNo(project = self, question = new_question))
      
      UserAnswerYesOrNo.objects.bulk_create(project_task_list)
      project_task_list = []  

    # End
    else:
      super(Project, self).save(*args, **kwargs)
  # COMMENT OUT AT NEW DEPLOY


