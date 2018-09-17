from django.db import models

class Challenge(models.Model):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  city = models.CharField(("City"), blank=True, max_length=150)

  # year
  # context
  # start_date
  # end_date

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  challenge_code = models.CharField(("Registration Code"),max_length=8, null=True, blank=True)
  # COMMENT OUT AT NEW DEPLOY
  
  def __str__(self):
    return self.city
