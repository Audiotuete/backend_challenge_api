from django.db import models
from django.utils.crypto import get_random_string

import datetime

class Challenge(models.Model):

  YEAR_CHOICES = [(r,r) for r in range(2018, datetime.date.today().year+2)]

  context = models.CharField(('Kontext (Schulen- / Kommunenname)'), blank=True, max_length=150)
  city = models.CharField(('Stadt'), blank=True, max_length=150)
  year = models.IntegerField(('Jahr'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
  start_date = models.DateField(('Start-Datum'),null=True, blank=True)
  end_date = models.DateField(('End-Datum'),null=True, blank=True)

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  challenge_code = models.CharField(('Challenge Code'),max_length=7, null=True, blank=True, unique=True)
  # COMMENT OUT AT NEW DEPLOY
  
  def __str__(self):
    return self.context

  def save(self, *args, **kwargs):
    # If Challenge doesn't already exist create a new Challenge
    if self.pk is None:

      self.challenge_code = get_random_string(length=7).upper()

      super(Challenge, self).save(*args, **kwargs)

    # End
    else:
      super(Challenge, self).save(*args, **kwargs)
