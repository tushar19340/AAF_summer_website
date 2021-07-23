import research_centers
from django.contrib import admin
from research_centers.models import Research_Center, Activity,photos



class BlogInline(admin.StackedInline):
    model = Activity
    extra = 0


class ResearchCenterAdmin(admin.ModelAdmin):
    inlines = [BlogInline]

admin.site.register(Research_Center, ResearchCenterAdmin)

admin.site.register(photos)