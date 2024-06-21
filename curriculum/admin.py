from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from curriculum.models import Lesson, Standard, Subject, Session, ClassGroup

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
   
    list_display=('name', 'term', 'start_date', 'end_date')
    exclude = ['slug']

class StandardAdmin(admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']

class ClassGroupAdmin(admin.ModelAdmin):
       
    list_display=('name', 'description',)
    exclude = ['slug']

class SubjectAdmin(admin.ModelAdmin):
       
    list_display=('subject_id', 'name', 'standard')
    exclude = ['slug']

class LessonAdmin(admin.ModelAdmin):
       
    list_display=(  'standard', 'subject', 'lesson_id', 'name' )
    list_filter = ['standard',]
    search_fields = ('standard__name', 'subject__name')
    raw_id_fields = ['created_by',]
    exclude = ['slug']



admin.site.register(Session, SessionAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)






class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

