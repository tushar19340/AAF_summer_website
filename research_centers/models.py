from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Research_Center(models.Model):
    name = models.CharField(max_length=250)
    image_url = CloudinaryField('image')
    short_description = models.TextField(blank=True, null=True)
    info = RichTextField()

    def __str__(self):
        return self.name
        

class Activity(models.Model):
    title = models.CharField(max_length=200)
    image_url = CloudinaryField('image')
    text = RichTextField()
    research_center = models.ForeignKey(Research_Center,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')