from django.contrib import admin
from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
       
    list_display=('exam_name', 'standard', 'subject_name')
    list_filter = ['standard']

admin.site.register(Quiz, QuizAdmin)