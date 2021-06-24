from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

class Career_Talk(models.Model):
    title=models.CharField(max_length=200)
    sub_text=models.TextField(null=True)
    video_link=models.CharField(max_length=100)
    image_url=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)