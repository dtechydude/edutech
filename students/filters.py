import django_filters
from .models import StudentDetail
from django.contrib.auth.models import User

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = StudentDetail
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'current_class', 'class_teacher', 'student_status'}
        

