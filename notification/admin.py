from django.contrib import admin
from .models import Notification, SchoolCalendar, Notifications, NotificationStudent

# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    list_display=('sender', 'date_sent', 'subject')
    list_filter  = ['student__current_class', 'staff__department']
    search_fields = ('sender__username',)
    raw_id_fields = ['sender',]

class NotificationStudentAdmin(admin.ModelAdmin):
    list_display=('sender', 'date_sent', 'subject')
    list_filter  = ['sender__current_class']
    search_fields = ('sender__username',)
    raw_id_fields = ['sender',]


class SchoolCalendarAdmin(admin.ModelAdmin):
    list_display=('event_name', 'event_date', 'duration')


admin.site.register(SchoolCalendar, SchoolCalendarAdmin)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(NotificationStudent, NotificationStudentAdmin)

