from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from app_tasks.models import TaskOpen, TaskYesOrNo, TaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple


class User(AbstractUser):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  name = CharField(_("Name of User"), blank=True, max_length=255)

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  # push_notifications = BooleanField(("Push notfications enabled"), default=True)
  # reg_code = CharField(("Registration Code"),max_length=8, null=True, blank=True)
  # COMMENT OUT AT NEW DEPLOY

  def get_absolute_url(self):
    return reverse("users:detail", kwargs={"username": self.username})
  
  def __str__(self):
    return self.username

  # COMMENT OUT AT NEW DEPLOY
  # def save(self, *args, **kwargs):
  #   # If Task doesn't already exist create an (empty) ProjectTask entry for each User in the database upfront.
  #   if self.pk is None:

  #     super(User, self).save(*args, **kwargs)
      
  #     open_tasks = TaskOpen.objects.all()
  #     multiple_choice_tasks = TaskMultiple.objects.all()
  #     yes_or_no_tasks = TaskYesOrNo.objects.all()

  #     usertask_list = []
 
  #     for new_task in open_tasks:
  #       usertask_list.append(ProjectTaskOpen(user = self, task = new_task))
  #     ProjectTaskOpen.objects.bulk_create(usertask_list)

  #     usertask_list = []
 
  #     for new_task in multiple_choice_tasks:
  #       usertask_list.append(ProjectTaskMultiple(user = self, task = new_task))
  #     ProjectTaskMultiple.objects.bulk_create(usertask_list)
      
  #     usertask_list = []  

  #     for new_task in yes_or_no_tasks:
  #       usertask_list.append(ProjectTaskYesOrNo(user = self, task = new_task))
      
  #     ProjectTaskYesOrNo.objects.bulk_create(usertask_list)
  #     usertask_list = []  

  #   # End
  #   else:
  #     super(User, self).save(*args, **kwargs)
  # COMMENT OUT AT NEW DEPLOY


