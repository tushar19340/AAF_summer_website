from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path("", views.courses),
    path("course_playlist", views.course_playlist),
    path("<int:course_id>/",views.details,name="details")
]