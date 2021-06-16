from django.contrib import admin
from django.urls import path, include
from career_talks import views

urlpatterns = [
    path("", views.career_talks),
    path("/id", views.career_talk_individual),
]