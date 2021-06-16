from django.shortcuts import render, HttpResponse
from career_talks import models

def career_talks(request):
    return render(request, 'career_talks/career_talks.html')

def career_talk_individual(request):
    return render(request, 'career_talks/career_talk_individual.html')
