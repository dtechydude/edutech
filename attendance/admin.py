from django.contrib import admin
from attendance.models import Attendance



class AttendanceAdmin(admin.ModelAdmin):

    list_display=('student_id', 'attendance_date', 'morning_status', 'afternoon_status')
    list_filter  = ['student_id__current_class']
    search_fields = ('student_id__user__username', 'student_id__last_name', 'student_id__first_name')
    raw_id_fields = ['student_id',]
  


admin.site.register(Attendance, AttendanceAdmin)



