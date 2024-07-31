from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class Calendar(models.Model):
    date = models.DateField()

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    guests = models.PositiveIntegerField()


    class Meta:
        unique_together = ('date', 'time_slot')
