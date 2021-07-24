from django.contrib import admin
from django.urls import path, include
from contests import views

urlpatterns = [
    path("", views.contests),
    path("submission/<int:submission_id>/like", views.SubmissionLike),
    path("<int:contest_id>/submit", views.ContestSubmit),
    path("<int:contest_id>", views.contests_individual),
    path("demo", views.demo),
]