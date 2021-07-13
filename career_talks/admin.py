from django.contrib import admin
from career_talks.models import Career_Talk, Category
# Register your models here.

class Career_Talk_Admin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Career_Talk, Career_Talk_Admin)
admin.site.register(Category)
