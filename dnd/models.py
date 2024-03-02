from django.contrib.auth.models import User
from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Stats'

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.ForeignKey(Stat, related_name='race',blank=True, null=True,on_delete=models.CASCADE)
    darkvision = models.BooleanField(default=False)
    #race = models.ForeignKey(Race, related_name='npc', on_delete=models.CASCADE)

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

class Enemy(models.Model):
    race = models.ForeignKey(Race, related_name='enemy', on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, related_name='enemy', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hp = models.IntegerField(null=True)
    str = models.IntegerField(null=True)
    dex = models.IntegerField(null=True)
    con = models.IntegerField(null=True)
    int = models.IntegerField(null=True)
    wis = models.IntegerField(null=True)
    cha = models.IntegerField(null=True)
    ac = models.IntegerField(null=True)
    speed = models.CharField(max_length=255, blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    actions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    invisible = models.BooleanField(default=False)

    pictures = models.URLField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Enemies'
    def __str__(self):
        return self.name



class Character(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name

