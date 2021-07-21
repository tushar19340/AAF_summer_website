from django.contrib import admin
from contests.models import Contest, Category, Question, Choice, Submission

class Contest_Admin(admin.ModelAdmin):
    filter_horizontal = ('category',)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'contest')
    
admin.site.register(Contest, Contest_Admin)
admin.site.register(Category)
admin.site.register(Submission, SubmissionAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
