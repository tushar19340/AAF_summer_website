from django.contrib import admin
from django.urls import path, include
from research_centers import views

urlpatterns = [
    path("", views.index, name="research_centers"),
    path("<int:center_id>/activities/<int:activity_id>", views.show_activity, name="get_research_center"),
    path("<int:center_id>/activities/", views.get_research_center_activities, name="get_research_center"),
    path("<int:center_id>/", views.get_research_center, name="get_center"),
]