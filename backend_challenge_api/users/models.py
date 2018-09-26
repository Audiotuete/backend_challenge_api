from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  name = models.CharField(_("Name of User"), blank=True, max_length=255)
  currentChallenge = models.ForeignKey('app_challenges.Challenge', on_delete=models.SET_NULL, null=True, blank=True)
  currentProject = models.ForeignKey('app_projects.Project', on_delete=models.SET_NULL, null=True, blank=True)


  def get_absolute_url(self):
    return reverse("users:detail", kwargs={"username": self.username})
  
  def __str__(self):
    return self.username
