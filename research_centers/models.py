from django.db import models
from ckeditor.fields import RichTextField



class Research_Center(models.Model):
    name = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    info = RichTextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=250)
    text = RichTextField()
    research_center = models.ForeignKey(Research_Center,on_delete=models.CASCADE)

    def __str__(self):
        return self.title