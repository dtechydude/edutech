from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from staff.models import Department, StaffCategory, StaffProfile
from users.models import Profile

# Register your models here.

# class ProfileInline(admin.TabularInline):
#     model = Profile
#     extra = 0



class StaffProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # inlines = [ProfileInline]   
    list_display=('staff_username', 'last_name', 'first_name', 'cat_name', 'class_in_charge', 'class_group')
    list_filter = ['class_in_charge']
    search_fields = ('first_name', 'last_name', 'staff_username')

class DepartmentAdmin(admin.ModelAdmin):
       
    list_display=('name', 'description',)
    exclude = ('slug',)




# admin.site.register(StaffCategory)
admin.site.register(StaffProfile, StaffProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
