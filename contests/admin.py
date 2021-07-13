from django.contrib import admin
from contests.models import Contest, Category

class Contest_Admin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Contest, Contest_Admin)
admin.site.register(Category)

