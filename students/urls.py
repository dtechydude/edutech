from django.urls import path
#from wkhtmltopdf.views import PDFTemplateView
from wkhtmltopdf import WKHtmlToPdf
from django.conf import settings
from django.conf.urls.static import static
from students import views as student_views 
from django.contrib.auth import views as auth_views
from students.views import (StudentListView,
                            StudentDetailView,
                            StudentCreateView,
                            StudentUpdateView,
                            StudentDeleteView,
                            MyStudentList,
                            # StudentResultUpdateView,
                            StudentCardDetailView,
                            GuardianListView,
)

app_name = 'students'

urlpatterns = [
   
    path('', student_views.studentlist, name="student-list"),
    path('student-register', student_views.studentregisterform, name="student-registration"),
    path('student-summary', student_views.student_summary, name="student-summary"),
    # path('pdf/<pk>/', student_views.student_render_pdf_view, name="student-pdf-view"),
    # path('student-list/', StudentListView.as_view(), name="all-students"),
    path('<int:id>/', StudentDetailView.as_view(), name="students-detail"), 
    # path('<int:pk>/', StudentCardDetailView.as_view(), name='my_idcard'),
    path('new-student/', StudentCreateView.as_view(), name="students-create"),
    path('<int:id>/update/', StudentUpdateView.as_view(), name="students-update"),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name="students-delete"),  

     path('guardian-list/', GuardianListView.as_view(), name="guardian-list"), 

    # path('<int:id>/result-update/', StudentResultUpdateView.as_view(), name="result-update"),

    path('pdf/<pk>/', student_views.student_render_pdf_view, name="student-pdf-view"),
    path('test-view/', student_views.render_pdf_view, name="test-view"),

    path('student-pdf', student_views.mystudent_pdf, name="student-pdf"),
    path('student-csv', student_views.mystudent_csv, name="student-csv"),

    # Search student detail app
    path('student-search/', student_views.student_search_list, name='student_search_list'),
    path('search/', student_views.search, name='search'),

    #for my rest_framework
    path('api-auth/', MyStudentList.as_view(), name="apiview"),
    
    #render id card as pdf
    path('idcard-pdf/<pk>/', student_views.id_render_pdf_view, name="idcard-pdf-view"),
    #path('idcard/', PDFTemplateView.as_view(template_name='students/student_id_card.html',
    #                                       filename='id_card.pdf'), name='id-card-pdf'),

]