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



class Gifter(models.Model):

    number = models.IntegerField(blank=True,null=True)
    created_by = models.ForeignKey(User, related_name='numbers', on_delete=models.CASCADE, null=True)


