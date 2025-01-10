from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from students.models import StudentDetail, Badge


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('student_username', 'last_name', 'first_name', 'current_class', 'class_group', 'date_admitted', 'guardian_phone')
    list_filter = ['current_class', 'class_group']
    search_fields = ('first_name', 'last_name', 'user__username')
    raw_id_fields = ['user', 'class_teacher', 'badge', 'class_group']
   

class BadgeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('name', 'description',)
    exclude=('slug',)


# Register your models here.
admin.site.register(StudentDetail, StudentAdmin)
admin.site.register(Badge, BadgeAdmin)

