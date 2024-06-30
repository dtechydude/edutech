from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from students.models import StudentDetail, Badge


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('user', 'last_name', 'current_class', 'date_admitted', 'guardian_phone')
    list_filter = ['current_class']
    search_fields = ('first_name', 'last_name', 'user__username')
    raw_id_fields = ['user', 'class_teacher', 'badge', 'class_group']
   

   

class BadgeAdmin(admin.ModelAdmin):
       
    list_display=('name', 'description',)


# Register your models here.
admin.site.register(StudentDetail, StudentAdmin)
admin.site.register(Badge, BadgeAdmin)

