from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

from ordered_model.models import OrderedModel
import datetime

class Challenge(models.Model):

  class Meta:
    indexes = [
        models.Index(fields=['challenge_code',]),
    ]

  YEAR_CHOICES = [(r,r) for r in range(2018, datetime.date.today().year+2)]

  # Relationships
  tasks =  models.ManyToManyField('app_tasks.Task', verbose_name='Aufgaben', blank=True) 
  contact_info = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Ansprechpartner_in', blank=True)

  # Fields
  context = models.CharField(('Kontext (Schule- / Kommune)'), blank=True, max_length=150)
  city = models.CharField(('Stadt'), blank=True, max_length=150)
  year = models.IntegerField(('Jahr'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
  start_date = models.DateField(('Start-Datum'), null=True, blank=True)
  end_date = models.DateField(('End-Datum'), null=True, blank=True)
  challenge_code = models.CharField(('Challenge Code'),max_length=5, blank=True, unique=True)
  
  def __str__(self):
    return self.context

  def save(self, *args, **kwargs):
    # If Challenge doesn't already exist create a new Challenge

    if self.pk is None:
      generated_code = get_random_string(length=5).lower()

      
      while Challenge.objects.filter(challenge_code = generated_code):
        generated_code = get_random_string(length=5).lower()

      self.challenge_code = generated_code

      super(Challenge, self).save(*args, **kwargs)

    # End
    else:    
      super(Challenge, self).save(*args, **kwargs)

class ChallengeDate(OrderedModel):

  class Meta:
    ordering = ('order',)
  order_class_path = __module__ + '.ChallengeDate'

  # Relationsships
  challenge = models.ForeignKey('app_challenges.Challenge', on_delete=models.PROTECT, null=True, blank=True)

  # Fields
  event_name = models.CharField(('Veranstaltung'), null=True, blank=True, max_length=150)
  event_location = models.CharField(('Ort'), null=True, blank=True, max_length=150)
  event_date = models.DateField(('Datum'), null=True, blank=True)
  event_start_time = models.TimeField(('Beginn'), null=True, blank=True)
  event_end_time = models.TimeField(('Ende'), null=True, blank=True)
  event_notes = models.CharField(('Anmerkungen'), null=True, blank=True, max_length=150)

  def __str__(self):
    return self.event_name