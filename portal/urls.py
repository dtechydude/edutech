from django.urls import path
from portal import views as portal_views 
from . import views


app_name = 'portal'

urlpatterns = [
    path('home/', portal_views.portal_home, name="portal-home"),
    path('register-class/', portal_views.register_new_standard, name="register-class"),
    path('register-class-section/', portal_views.register_new_classgroup, name="register-classgroup"),
    path('register-new-session/', portal_views.register_new_session, name="register-session"),
    path('register-new-category/', portal_views.register_new_category, name="register-category"),
    path('register-new-department/', portal_views.register_new_department, name="register-department"),
    path('register-new-subject/', portal_views.register_exam_subjects, name="register-subject"),
    path('register-exam/', portal_views.register_exam, name="register-exam"),
    path('<int:pk>/', views.StudentCardDetailView.as_view(), name='my_idcard'),

    path('category-list/', views.CategoryListView.as_view(), name="category_list"),
    path('department-list/', views.DepartmentListView.as_view(), name="department_list"),
    path('subjects-list/', views.SubjectListView.as_view(), name="subject_list"),
    path('exam-list/', views.ExamListView.as_view(), name="exam_list"),
    path('session-list/', views.SessionListView.as_view(), name="session_list"),
    path('class-group-list/', views.ClassGroupListView.as_view(), name="classgroup_list"),
    path('exam/', portal_views.set_exam, name='set-exam'), 
   


]
