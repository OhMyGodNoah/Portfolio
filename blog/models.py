import os

from django.db import models

# Create your models here.
current_dir = os.getcwd()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=current_dir + '/media/images')
    summary = models.TextField(max_length=10000)
    date = models.DateField()

    def __str__(self):
        return self.title

    def short(self):
        return self.summary[:100]
