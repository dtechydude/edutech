from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def schoolly_home(request):
    return render(request, 'pages/schoollyedtech.html')
