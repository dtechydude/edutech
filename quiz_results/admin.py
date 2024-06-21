from django.contrib import admin
from .models import QuizResult
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# class QuizResultAdmin(admin.ModelAdmin):
class QuizResultAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('quiz', 'user', 'subject', 'score', 'exam_score', 'ca_score')
    list_filter  = ['quiz__subject_name', 'quiz__standard__name',]
    search_fields = ('user__username',)


admin.site.register(QuizResult, QuizResultAdmin)



