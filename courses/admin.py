from django.contrib import admin
from courses.models import Course, Category


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)

