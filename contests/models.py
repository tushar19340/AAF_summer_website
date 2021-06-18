from django.db import models

# Create your models here.
def Item():
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    start_date=models.DateField()
    end_date=models.DateField()

def Category():
    name=models.CharField(max_length=100)

