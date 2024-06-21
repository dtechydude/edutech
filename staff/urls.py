from django.urls import path
from django.conf.urls.static import static
from staff import views as user_views 
from django.contrib.auth import views as auth_views
from .views import StaffDetailView, StaffUpdateView, StaffDeleteView, StaffListView

app_name = 'staff'

urlpatterns = [
    path('staff-form/', user_views.staffupdateprofile, name="staff_form"),
    path('staff-create/', user_views.staffprofile, name="staff_create"),
    # path('staff-academic/', user_views.staffacademic, name="staff-academic"),
    path('staff-list', user_views.stafflist, name="staff_list"),
    path('my-students/', user_views.self_student_list, name="my-students"),
    path('my-students-attendance/', user_views.self_student_attendance, name="my-students-attendance"),
    # path('', StaffListView.as_view(), name="staff_list"),
    path('<str:id>/', StaffDetailView.as_view(), name="staff_detail"),
    path('<int:id>/update/', StaffUpdateView.as_view(), name="staff_update"),
    path('<int:id>/delete/', StaffDeleteView.as_view(), name="staff_delete"), 
    path('staff-pdf', user_views.staff_pdf, name="staff-pdf"),
    path('staff-csv', user_views.staff_csv, name="staff-csv"),

]