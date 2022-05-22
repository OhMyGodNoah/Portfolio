import os

from django.db import models

# Create your models here.
current_dir = os.getcwd()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=current_dir + '/media/images')
    summary = models.CharField(max_length=200)
    date = models.DateField()
