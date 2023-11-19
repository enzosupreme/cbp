from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Key(models.Model):
    adafruit_username = models.CharField(max_length=75)
    adafruit_key = models.CharField(max_length=75)