from django import forms
from .models import Attendance
from students.models import StudentDetail



class StudentAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields = ['student_id', 'session', 'attendance_date', 'morning_status', 'afternoon_status', 'authorized_sign']
        widgets = {
            'attendance_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }

class MyStudentAttendanceForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['student_id'].queryset = StudentDetail.objects.filter(class_teacher__user=request.user).order_by('student_username')
    #     # self.fields['student_id'].queryset = Attendance.objects.filter(student_id__class_teacher__user=request.user)
    
    class Meta:
        model = Attendance
        def __init__(self, *args, **kwargs):
            student_id = kwargs.pop('student_id', None)
            super(MyStudentAttendanceForm, self).__init__(*args, **kwargs)
        
        fields = '__all__'
        widgets = {
            'attendance_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
        }



   
