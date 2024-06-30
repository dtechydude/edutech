from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from curriculum.models import Standard, Session
from students.models import StudentDetail



class Attendance(models.Model):
    student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE, blank=True, null=True)
    # standard = models.ForeignKey(Standard, on_delete=models.CASCADE, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True, default='2023/2024')
    attendance_date = models.DateField(null=True)
    morning_status = models.BooleanField(default=False)
    afternoon_status = models.BooleanField(default=False)
    authorized_sign = models.CharField(max_length=20, default='none')
    date_taken = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        unique_together = ['student_id', 'attendance_date', 'session',]
    
    def __str__ (self):
        return f'{self.student_id}'

