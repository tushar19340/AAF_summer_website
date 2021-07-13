from django.contrib import admin
from django.urls import path, include
from contests import views

urlpatterns = [
    path("", views.contests),
    path("<int:contest_id>", views.contests_individual),
]