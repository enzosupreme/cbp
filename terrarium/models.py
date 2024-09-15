from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=2555)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='plant_images', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.name

class Terrarium(models.Model):
    name = models.CharField(max_length=2555)
    image = models.ImageField(upload_to='terrarium_images', blank=True, null=True)
    plant1 = models.ForeignKey(Plant, related_name='plant', on_delete=models.CASCADE)
    plant2 = models.ForeignKey(Plant, related_name='plant2', on_delete=models.CASCADE)
    plant3 = models.ForeignKey(Plant, related_name='plant3', on_delete=models.CASCADE, blank=True, null=True)
    plant4 = models.ForeignKey(Plant, related_name='plant4', on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.name
