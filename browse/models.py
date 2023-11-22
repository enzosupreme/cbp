from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Key(models.Model):
    adafruit_username = models.CharField(max_length=75)
    adafruit_key = models.CharField(max_length=75)

class Santa(models.Model):
    name = models.CharField(max_length=75)
    def __str__(self):
        return self.name

class Gift(models.Model):
    name = models.CharField(max_length=75,blank=True,null=True)
    number = models.IntegerField(max_length=255,blank=True,null=True)
    password = models.CharField(max_length=75,blank=True,null=True)

    def __str__(self):
        return self.name
