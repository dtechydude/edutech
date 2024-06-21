import django_filters
from .models import StaffProfile
from django.contrib.auth.models import User

class StaffFilter(django_filters.FilterSet):

    class Meta:
        model = StaffProfile
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'staff_role', 'class_in_charge', 'department'}
        

