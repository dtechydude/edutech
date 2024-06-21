from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from students.models import StudentDetail
from staff.models import StaffProfile, StaffCategory, Department
from results.models import ExamSubject, Examination
from curriculum.models import Session, ClassGroup
from notification.models import SchoolCalendar
from django.views.generic import  ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ClassRegisterForm, ClassgroupRegisterForm, SessionRegisterForm, ExamRegisterForm, CategoryRegisterForm, DepartmentRegisterForm, SubjectRegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def portal_home(request):
    # if request.user.studentdetail.is_student:
    users_num = User.objects.count()
    student_num = StudentDetail.objects.count()
    num_student_inclass = StudentDetail.objects.filter().count()
    graduated = StudentDetail.objects.filter(student_status='graduated').count()
    dropped = StudentDetail.objects.filter(student_status='dropped').count()
    expelled = StudentDetail.objects.filter(student_status='expelled').count()
    suspended = StudentDetail.objects.filter(student_status='suspended').count()
    active = StudentDetail.objects.filter(student_status='active').count()
    staff_num = StaffProfile.objects.count()
    my_idcard = StudentDetail.objects.filter(user=User.objects.get(username=request.user))
    students = StudentDetail.objects.filter().order_by('current_class').values('current_class__name').annotate(count=Count('current_class__name'))
    my_students = StudentDetail.objects.filter(class_teacher__user=request.user).order_by('student_username')
    try:
        num_inclass = StudentDetail.objects.filter(current_class__name = request.user.studentdetail.current_class).count()
    except StudentDetail.DoesNotExist:
        num_inclass = StudentDetail.objects.filter()
    # Build a paginator with function based view
    queryset = SchoolCalendar.objects.all().order_by("-id")
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 40)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    context = {
        'student_num': student_num,
        'students' : students,
        'users_num': users_num,
        'num_inclass': num_inclass,
        'staff_num': staff_num,
        'graduated': graduated,
        'dropped': dropped,
        'expelled': expelled,
        'suspended': suspended,
        'active': active,
        'queryset': queryset,
        'events':events,
        'my_idcard':my_idcard,
        'my_students':my_students,
    }
    
    return render(request, 'portal/portal-home.html', context)


@login_required
def register_new_standard(request):
    if request.method == 'POST':
        
        new_class_form = ClassRegisterForm(request.POST)
        if new_class_form.is_valid():
           
            new_class_form.save()
            messages.success(request, f'New Class Registered successfully, Register another or go to class list')
            return redirect('portal:register-class')
    else:
      
        new_class_form = ClassRegisterForm

    context = {
        
        'new_class_form': new_class_form,
    }

    return render(request, 'portal/register_new_standard.html', context)

# Section/Classgroup Registration
@login_required
def register_new_classgroup(request):
    if request.method == 'POST':
        
        new_class_group = ClassgroupRegisterForm(request.POST)
        if new_class_group.is_valid():
           
            new_class_group.save()
            messages.success(request, f'New Class Group Registered successfully, Register another or go to classgroup list')
            return redirect('portal:register-classgroup')
    else:
      
        new_class_group = ClassgroupRegisterForm

    context = {
        
        'new_class_group': new_class_group,
    }

    return render(request, 'portal/register_new_classgroup.html', context)


@login_required
def register_new_session(request):
    if request.method == 'POST':
        
        new_session = SessionRegisterForm(request.POST)
        if new_session.is_valid():
           
            new_session.save()
            messages.success(request, f'New Session Registered successfully, Register another or go to session list')
            return redirect('portal:register-session')
    else:
      
        new_session = SessionRegisterForm

    context = {
        
        'new_session': new_session,
    }

    return render(request, 'portal/register_new_session.html', context)


@login_required
def register_exam(request):
    if request.method == 'POST':
        
        new_exam = ExamRegisterForm(request.POST)
        if new_exam.is_valid():
           
            new_exam.save()
            messages.success(request, f'New Exam Registered successfully, Register another or go to Exam list')
            return redirect('portal:register-exam')
    else:
      
        new_exam = ExamRegisterForm

    context = {
        
        'new_exam': new_exam,
    }

    return render(request, 'portal/register_exam.html', context)

# Register Department For Staff
@login_required
def register_new_department(request):
    if request.method == 'POST':
        
        new_department = DepartmentRegisterForm(request.POST)
        if new_department.is_valid():
           
            new_department.save()
            messages.success(request, f'New Department Registered successfully, Register another or go to department list')
            return redirect('portal:department_list')
    else:
      
        new_department = DepartmentRegisterForm

    context = {
        
        'new_department': new_department,
    }

    return render(request, 'portal/register_new_department.html', context)

# Register Category For Staff
@login_required
def register_new_category(request):
    if request.method == 'POST':
        
        new_category = CategoryRegisterForm(request.POST)
        if new_category.is_valid():
           
            new_category.save()
            messages.success(request, f'New Department Category successfully, Register another or go to category list')
            return redirect('portal:category_list')
    else:
      
        new_category = CategoryRegisterForm

    context = {
        
        'new_category': new_category,
    }

    return render(request, 'portal/register_new_category.html', context)

@login_required
def register_exam_subjects(request):
    if request.method == 'POST':
        
        new_subject = SubjectRegisterForm(request.POST)
        if new_subject.is_valid():
           
            new_subject.save()
            messages.success(request, f'New Subject Registered successfully, Register another or go to Subject list')
            return redirect('portal:subject_list')
    else:
      
        new_subject = SubjectRegisterForm

    context = {
        
        'new_subject': new_subject,
    }

    return render(request, 'portal/register_exam_subjects.html', context)


    
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


class CategoryListView(LoginRequiredMixin, ListView):
    context_object_name = 'categorylist'
    model = StaffCategory
    queryset = StaffCategory.objects.all()
    template_name = 'portal/category.html'
    paginate_by = 10


class DepartmentListView(LoginRequiredMixin, ListView):
    context_object_name = 'departmentlist'
    model = Department
    queryset = Department.objects.all()
    template_name = 'portal/department.html'
    paginate_by = 10

class SubjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'subjectlist'
    model = ExamSubject
    queryset = ExamSubject.objects.all()
    template_name = 'portal/subjects_list.html'
    paginate_by = 30


class ExamListView(LoginRequiredMixin, ListView):
    context_object_name = 'examlist'
    model = Examination
    queryset = Examination.objects.all()
    template_name = 'portal/exam_list.html'
    paginate_by = 30


class SessionListView(LoginRequiredMixin, ListView):
    context_object_name = 'sessionlist'
    model = Session
    queryset = Session.objects.all()
    template_name = 'portal/session_list.html'
    paginate_by = 30

class ClassGroupListView(LoginRequiredMixin, ListView):
    context_object_name = 'classgrouplist'
    model = ClassGroup
    queryset = ClassGroup.objects.all()
    template_name = 'portal/classgroup_list.html'
    paginate_by = 30