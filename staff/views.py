from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from staff.forms import StaffRegisterForm, StaffUpdateForm
from staff.models import StaffProfile
from students.models import StudentDetail
from curriculum.models import Standard
#from attendance.models import Attendance
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import UserUpdateForm, UserRegisterForm
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Count
# For Filter
from .filters import StaffFilter
from django_filters.views import FilterView
# For panigation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# for csv
import csv

# Create your views here.


@login_required
def staffupdateprofile(request):
    if request.method == 'POST':
        
        aca_form = StaffRegisterForm(request.POST)
        if aca_form.is_valid():
           
            aca_form.save()
            messages.success(request, f'New Staff Registered successfully')
            return redirect('staff:staff_detail')
    else:
      
        aca_form = StaffRegisterForm

    context = {
        
        'aca_form': aca_form,
    }

    return render(request, 'staff/staff_register_form.html', context)


@login_required
def stafflist(request):
    stafflist = StaffProfile.objects.all()
    staffprofile_filter = StaffFilter(request.GET, queryset=stafflist) 
    stafflist = staffprofile_filter.qs
    
    # PAGINATOR METHOD
    page = request.GET.get('page', 1)
    paginator = Paginator(stafflist, 40)
    try:
        stafflist = paginator.page(page)
    except PageNotAnInteger:
        stafflist = paginator.page(1)
    except EmptyPage:
        stafflist = paginator.page(paginator.num_pages)

    context = {
        'stafflist' : StaffProfile.objects.all(),
        'staffprofile_filter': staffprofile_filter,
        'stafflist': stafflist,

    }
    return render (request, 'staff/staff_list.html', context)

#teachers seeing the students in their class
@login_required
def self_student_list(request):
    my_students = StudentDetail.objects.filter(class_teacher__user=request.user).order_by('student_username')
    
    context = {
        'my_students': my_students
    }

    return render (request, 'staff/my_students.html', context)


@login_required
def self_student_attendance(request):
    my_students_attendance = Attendance.objects.filter(student_id__class_teacher__user=request.user).order_by('student_id')
    att_count = Attendance.objects.values('student_id__first_name').annotate(c=Count('student_id__first_name')).order_by('-c')
    student_att = Attendance.objects.filter().order_by('student_id').values('student_id__last_name').annotate(count=Count('student_id__last_name'))
    my_own_students = StudentDetail.objects.filter(class_teacher__user=request.user).order_by('student_username')
    my_student_att = Attendance.objects.filter(student_id__class_teacher__user=request.user).order_by('student_id').values('student_id__last_name').annotate(count=Count('student_id__last_name'))

    # PAGINATOR
    page = request.GET.get('page', 1)
    paginator = Paginator(my_students_attendance, 30)
    try:
        my_students_attendance = paginator.page(page)
    except PageNotAnInteger:
        my_students_attendance = paginator.page(1)
    except EmptyPage:
        my_students_attendance = paginator.page(paginator.num_pages)


    
    context = {
        'my_students_attendance': my_students_attendance,
        'att_count' : Attendance.objects.values('student_id__first_name').annotate(c=Count('student_id__first_name')).order_by('-c'),
        'student_att' : student_att,
        'my_own_students': my_own_students,
        'my_student_att' : my_student_att

    }

    return render (request, 'staff/my_students_attendance.html', context)
    # return render (request, 'staff/att_test.html', context)




class StaffListView(LoginRequiredMixin, ListView):
    context_object_name = 'stafflist'
    model = StaffProfile
    queryset = StaffProfile.objects.all()
    template_name = 'staff/staff_list.html'
    paginate_by = 10
    # filterset_class = StaffFilter
    


# Generate a PDF staff list
def staff_pdf(request):
    # create Bytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)
    # Add some lines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line31",
    #     "This is line 4",
    # ]
    # Designate the model
    staff = StaffProfile.objects.all()

    # Create a blank list
        
    lines = [" Staff List Report"]

    for staffs in staff:
        lines.append(""),
        lines.append("Username: " + staffs.user.username),
        lines.append("Qualification: " + staffs.qualification),
        # lines.append("Year: " + staffs.year),
        lines.append("Institution: " + staffs.institution),
        lines.append ("Marital_Status: " + staffs.marital_status),
        lines.append("Phone: " + staffs.phone),
        lines.append("========="),


    # loop
    for line in lines:
        textob.textLine(line)
    #fininsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something
    return FileResponse(buf, as_attachment=False, filename='staff.pdf')


# Generate a CSV staff list
def staff_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=staff.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    staff = StaffProfile.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['USERNAME', 'FIRST NAME', 'LAST NAME', 'GENDER', 'DATE EMPLOYED', 'PHONE', 'EMAIL', 'QUALIFICATION', 'CLASS-IN-CHARGE'])


    # Loop thru and output
    for staffs in staff:
        writer.writerow([staffs.user.username, staffs.first_name, staffs.last_name, staffs.gender, staffs.date_employed, staffs.phone, staffs.user.email, staffs.qualification, staffs.class_in_charge])
        
    return response


class StaffDetailView(DetailView):
    template_name = 'staff/staff_details.html'
    # queryset = StaffProfile.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StaffProfile, id=id_)


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StaffUpdateForm
    template_name = 'staff/staff_update_form.html'
    # queryset = StudentDetail.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StaffProfile, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class StaffDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'staff/staff_delete.html'
    success_url = reverse_lazy('staff:staff_list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StaffProfile, id=id_)
    # queryset = StudentDetail.objects.all()

   

@login_required
def staffprofile(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST,)
        staff_form = StaffRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and staff_form.is_valid():
            u_form.save()
            staff_form.save()
            messages.success(request, f'New Staff Registered Successfully Please Profile Immediately!')
            return redirect('staff:staff_list')
    else:
        u_form = UserRegisterForm()
        staff_form = StaffRegisterForm()

    context = {
        'u_form': u_form,
        'staff_form': staff_form,
    }

    return render(request, 'staff/staff_register_form.html', context)
