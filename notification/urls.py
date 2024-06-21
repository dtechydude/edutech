from django.urls import path
from . import views
from notification import views as notification_views
from .views import NotificationListView, NotificationDetailView, NotificationCreateView, NotificationStudentCreateView, NotificationStudentDetailView



app_name = 'notification'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name="mail-list"),
    path('self-mail/', notification_views.view_self_notification, name="mail-self"),
    path('self-mail/<int:pk>/', NotificationDetailView.as_view(), name='mail-detail'),
    #student self notification
    # path('student-mail/', notification_views.student_send_notification, name="mail-student"),
    path('admin-mail/', notification_views.admin_view_notification, name="admin-mail"),

    path('new-mail/', NotificationCreateView.as_view(), name='new-mail'),
    path('student-mail/', NotificationStudentCreateView.as_view(), name='student-mail'),
    path('student-mail/<int:pk>/', NotificationStudentDetailView.as_view(), name='student-mail-detail'),
    path('calendar/', notification_views.school_calendar, name="calendar"),
    path('calendar-form/', notification_views.school_calendar_form, name="calendar-form"),
    

    
      
   
]
