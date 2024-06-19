from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



from staff.models import Department, StaffCategory, StaffProfile

# Register your models here.
class StaffProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('staff_username', 'last_name', 'first_name', 'cat_name', 'class_in_charge', 'class_group')
    list_filter = ['class_in_charge']
    search_fields = ('first_name', 'last_name', 'staff_username')

admin.site.register(StaffCategory)
admin.site.register(StaffProfile, StaffProfileAdmin)
# admin.site.register(StaffAcademicInfo)
admin.site.register(Department)
