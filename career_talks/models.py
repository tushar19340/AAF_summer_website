from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    
class Career_Talk(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextField("Description", null = True)
    embeded_video_link = models.TextField(blank=True, null=True)
    image_url = CloudinaryField('image')
    date_added = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, null=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = 'Career Talks'

    def __str__(self):
        return self.title