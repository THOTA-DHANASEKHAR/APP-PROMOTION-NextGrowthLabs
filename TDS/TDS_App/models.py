from django.db import models

class AppDetails(models.Model):
    AppIcon = models.ImageField(upload_to='AppIcons')
    AppName = models.CharField(max_length=100)
    AppLink = models.CharField(max_length=100)
    AppCategory = models.CharField(max_length=100)
    AppSubCategory = models.CharField(max_length=100)
    points = models.IntegerField(default=1)

