from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]    
    list_display=('text', 'quiz')
    list_filter  = ['quiz__standard', 'quiz']
    search_fields = ('text',)
    


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
