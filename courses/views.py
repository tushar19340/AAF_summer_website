from django.shortcuts import render, HttpResponse
from courses import models

def courses(request):
    questions = models.Question.objects.all()
    
    context = {
        "questions": questions[1]
    }
    return render(request, 'courses/courses.html', context)

def course_playlist(request):
    questions = models.Question.objects.all()
    
    context = {
        "questions": questions[1]
    }
    return render(request, 'courses/course_playlist.html', context)
