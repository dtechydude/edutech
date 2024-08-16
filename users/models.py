from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import generate_ref_code
from staff.models import StaffProfile
from students.models import StudentDetail


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=20, blank=True, null=True)

    select = 'Select'
    southwest = 'SouthWest'
    southeast = 'SouthEast'
    southsouth = 'SouthSouth'
    northwest = 'NorthWest'
    northeast = 'NorthEast'
    northcentral = 'NorthCentral'
    
    region_origin = [
        ('Select', select),
        ('SouthWest', southwest),
        ('SouthEast', southeast),
        ('SouthSouth', southsouth),
        ('NorthWest', northwest),
        ('NorthEast', northeast),
        ('NorthCentral', northcentral),
    ]

    region_origin = models.CharField(max_length=15, choices=region_origin, default=select)

    bio = models.TextField(max_length=150, blank=True)
    code = models.CharField(max_length=6, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
   
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    admin = 'admin'
    inactive = 'inactive'
 

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
        (admin, 'admin'),
        (inactive, 'inactive'),
      
    ]

    user_type = models.CharField(max_length=15, choices=user_types, default=inactive)

    class Meta:
        ordering = ['user']


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'username:- {self.user.username} - {self.user.email}'

    
    def save(self, *args, **kwargs):
        if self.code =="":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)

    