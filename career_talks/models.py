from django.db import models

# Create your models here.
def Category():
    name=models.CharField(max_length=50)

def Item():
    title=models.CharField(max_length=200)
    sub_text=models.CharField(max_length=1000)
    video_link=models.CharField(max_length=100)
    image_url=models.CharField(max_length=100)
