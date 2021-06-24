from django.db import models

# Create your models here.
class Contest(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True)
    start_date=models.DateField()
    end_date=models.DateField()

class Category(models.Model):
    name=models.CharField(max_length=100)

