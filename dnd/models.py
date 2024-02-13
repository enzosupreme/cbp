from django.contrib.auth.models import User
from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.name

class Affiliation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Affiliations'
    def __str__(self):
        return self.name

class NonPlayerCharacter(models.Model):
    race = models.ForeignKey(Race, related_name='npc', on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, related_name='npc', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    invisible = models.BooleanField(default=False)

    pictures = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'NPCs'
    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name

