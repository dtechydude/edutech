from django.urls import path
from attendance import views as attendance_views



app_name = 'attendance'

urlpatterns = [
    
    path('attendance-form/', attendance_views.student_attendance, name='attendance_form'),
    path('my-std-att-form/', attendance_views.my_student_att_form, name='my-std-att-form'),
    path('attendance-view/', attendance_views.attendance_view, name='attendance_view'),

    # path('pdf/<pk>/', attendance_views.attendance_render_pdf_view, name="attendance-pdf-view"),

    # path('attendance-pdf', attendance_views.attendance_pdf, name="attendance-pdf"),
    path('attendance-csv', attendance_views.attendance_csv, name="attendance-csv"),
 
    
]
