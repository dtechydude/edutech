from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def schoolly_home(request):
    return render(request, 'pages/schoollyedtech.html')

@login_required
def set_exam(request):
    return render(request, 'exams/set_exam.html')
