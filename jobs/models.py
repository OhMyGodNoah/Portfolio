import os

from django.db import models

current_dir = os.getcwd()
parent = os.path.dirname(current_dir)


class Job(models.Model):
    image = models.ImageField(upload_to=current_dir + '/media/images')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
