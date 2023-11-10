from django.db import models

# Create your models here.

class GalleryItem(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=255)
