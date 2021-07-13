from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField("Short Description",max_length=200, null=True)
    info = RichTextField("Information of Contest", null=True)
    image_url = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ManyToManyField(Category, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


