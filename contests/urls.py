from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path("", views.courses),
    path("/id", views.courses),
]