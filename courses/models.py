from django.db import models



class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Question(models.Model):
    choice = models.ManyToManyField(Choice, blank = True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True)
    playlist_link=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    image_link=models.CharField(max_length=200)

    @staticmethod
    def getCourses():
        return Course.objects.all()
