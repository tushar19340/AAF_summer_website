from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField("Course decription", max_length=200)
    playlist_id = models.CharField("Youtube playlist url", max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image_link = CloudinaryField('image')
    category = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return self.title


    # @staticmethod
    # def getCourses():
    #     return Course.objects.all()
