from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    subject = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, null=True)


class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    invisible = models.BooleanField(default=False)
    github = models.URLField(max_length=200, blank=True, null=True)
    pictures = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    shop = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.name


class Menu_item(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name

class Image(models.Model):
    projects = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)

class Garden_Pic(models.Model):
    image = models.ImageField(upload_to='project_images', blank=True, null=True)