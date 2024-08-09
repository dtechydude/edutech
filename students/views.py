from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Count
#converting html to pdf
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from students.models import StudentDetail
from students.forms import StudentUpdateForm, StudentRegisterForm
from users.forms import UserRegisterForm
from curriculum.models import Standard
from results.models import ResultSheet
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
import csv
# for my rest_framework
from .serializers import StudentDetailSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# For Filter
from .filters import StudentFilter
from django_filters.views import FilterView
# For panigation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa



@login_required
def studentregisterform(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST,)
        student_form = StudentRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and student_form.is_valid():
            u_form.save()
            student_form.save()
            messages.success(request, f'New Student Registered Successfully, Please Profile the student!')
            return redirect('students:student-list')
            # return HttpResponseRedirect('')
    else:
        u_form = UserRegisterForm()
        student_form = StudentRegisterForm()

    context = {
        'u_form': u_form,
        'student_form': student_form,
    }

    return render(request, 'students/student_register_form.html', context)


@login_required
def studentupdateform(request):
    if request.method == 'POST':
        su_form = StudentUpdateForm(request.POST)
        #
      
        if su_form.is_valid():    #and sa_form.is_valid():
            su_form.save()
         #
            
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
         su_form = StudentUpdateForm()
        #
       
            
    context = {
        'su_form': su_form,
        #
   
    }

    return render(request, 'students/student_register_form.html', context)


@login_required
def studentlist(request):
    studentlist = StudentDetail.objects.all().order_by('-date_admitted')
    studentdetail_filter = StudentFilter(request.GET, queryset=studentlist) 
    studentlist = studentdetail_filter.qs

     # PAGINATOR METHOD
    page = request.GET.get('page', 1)
    paginator = Paginator(studentlist, 40)
    try:
        studentlist = paginator.page(page)
    except PageNotAnInteger:
        studentlist = paginator.page(1)
    except EmptyPage:
        studentlist = paginator.page(paginator.num_pages)

    context = {
        'studentlist' : StudentDetail.objects.all(),
        'studentdetail_filter': studentdetail_filter,
        'studentlist' : studentlist,
       

    }
    return render (request, 'students/student_list.html', context)


@login_required
def student_summary(request):
    standard = Standard.objects.all()
    students = StudentDetail.objects.filter().order_by('current_class').values('current_class__name').annotate(count=Count('current_class__name'))
    studentreport = StudentDetail.objects.all()
    num_inclass = Standard.objects.filter().count()

    context = {
        'studentreport' : StudentDetail.objects.all(),
        'num_inclass' :num_inclass,
        'students': students
        # 'studentdetail_filter': studentdetail_filter,
        # 'studentlist' : studentlist,
       
    }
    return render (request, 'students/student_summary.html', context)




class StudentListView(LoginRequiredMixin, ListView):
    context_object_name = 'students'
    model = StudentDetail
    queryset = StudentDetail.objects.all()
    template_name = 'students/student_list.html'
    paginate_by = 20
    filterset_class = StudentFilter
    


class StudentDetailView(LoginRequiredMixin, DetailView):  
    model = StudentDetail
    template_name = 'students/student_detail_view.html'
    # queryset = User.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StudentDetail, id=id_)

#generate IDCARD PDF
@login_required
def id_render_pdf_view(request, *args, **kwargs):    

    pk = kwargs.get('pk')
    
    student_detail = get_object_or_404(StudentDetail, pk=pk)
    template_path = 'students/student_id_pdf.html'
    # template_path = 'results/result_sheet.html'
    context = {'student_detail': student_detail}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you want to download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you just want to display
    response['Content-Disposition'] = 'filename="id_card.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# I am using function base view as above instead of this
class StudentCreateView(LoginRequiredMixin, CreateView):
    form_class = StudentRegisterForm
    template_name = 'students/student_register_form.html'
    # queryset= StudentDetail.objects.all()

    # success_url = '/'
    def form_valid(self, form):
        return super().form_valid(form)



class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentUpdateForm
    template_name = 'students/student_update_form.html'
    # queryset = StudentDetail.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StudentDetail, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'students/student_delete.html'
    success_url = reverse_lazy('students:student-list')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StudentDetail, id=id_)
    # queryset = StudentDetail.objects.all()


def student_render_pdf_view(request, *args, **kwargs):    

    pk = kwargs.get('pk')
    
    student = get_object_or_404(StudentDetail, pk=pk)
    template_path = 'students/pdf2.html'
    context = {'student': student}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you want to download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you just want to display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# redering pdf function
def render_pdf_view(request):
    template_path = 'students/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you want to download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you just want to display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def studentpage(request):

    return render(request, 'students/student_page.html', {})



# Generate a PDF staff list
def mystudent_pdf(request):
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
    student = StudentDetail.objects.all()

    # Create a blank list
        
    lines = [" Student List Report"]

    for students in student:
        lines.append(""),
        lines.append("Username: " + students.student_username),
        lines.append("Current Class: " + str(students.current_class)),
        lines.append("Class Teacher: " + str(students.class_teacher.user.username)), 
        lines.append("Student Type: " + students.student_type),
        lines.append("-------------------------------------"),


    # loop
    for line in lines:
        textob.textLine(line)
    #fininsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something
    return FileResponse(buf, as_attachment=False, filename='students.pdf')


# Generate a CSV staff list
def mystudent_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=student.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    students = StudentDetail.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['USERNAME', 'FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER', 'CURRENT CLASS', 'ADMISSION DATE', 'CLASS TEACHER', 'STUDENT TYPE', 'STATUS', 'PARENT PHONE'])


    # Loop thru and output
    for student in students:
        writer.writerow([student.student_username, student.first_name, student.middle_name, student.last_name, student.gender, student.current_class, student.date_admitted, student.class_teacher, student.student_type, student.student_status, student.guardian_phone])
        
    return response




def studentupdate(request):
    if request.method == 'POST':
        student_form = StudentUpdateForm(request.POST)
       
        if student_form.is_valid():
            student_form.save()
            messages.success(request, f'Your profile has been updated successfully')
            return redirect('profile')
    else:
        student_form = StudentUpdateForm()
       

    context = {
        'student_form': student_form,

    }

    return render(request, 'users/student_update_form.html', context)


class StudentCardDetailView(LoginRequiredMixin, DetailView):
    model = StudentDetail
    context_object_name = 'my_idcard'
    template_name = 'students/student_id_card.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        new_str = self.kwargs.get('pk') or self.request.GET.get('pk') or None

        queryset = queryset.filter(pk=new_str)
        obj = queryset.get()
        return obj


# Student Search Query App

def student_search_list(request):
    student = StudentDetail.objects.all()
    
     # PAGINATOR METHOD
    page = request.GET.get('page', 1)
    paginator = Paginator(student, 30)
    try:
        student = paginator.page(page)
    except PageNotAnInteger:
        student = paginator.page(1)
    except EmptyPage:
        student = paginator.page(paginator.num_pages)

    return render(request, 'students/search_student_list.html', {'student': student })

# Define function to search student
def search(request):
    results = []

    if request.method == "GET":
        query = request.GET.get('search')

        if query == '':
            query = 'None'

        results = StudentDetail.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(guardian_name__icontains=query) | Q(class_teacher__first_name__icontains=query) | Q(current_class__name__icontains=query))

        
    return render(request, 'students/search.html', {'query': query, 'results': results})


class GuardianListView(LoginRequiredMixin, ListView):
    context_object_name = 'guardian'
    model = StudentDetail
    queryset = StudentDetail.objects.all()
    template_name = 'students/guardian_list.html'
    paginate_by = 50
    filterset_class = StudentFilter


class MyStudentList(APIView):

    def get(self, request):
        students1 = StudentDetail.objects.all().order_by('-date_admitted')
        serializer = StudentDetailSerializer(students1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass


