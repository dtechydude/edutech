from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from curriculum.models import Standard, ClassGroup
from django.urls import reverse
from staff.models import StaffProfile

class Badge(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__ (self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StudentDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='student_username', blank=True, null=True)
    student_username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(blank=True, null=True, verbose_name='Date of Birth (YYYY-MM-DD)')

    female = 'female'
    male = 'male'
    select_gender = 'select_gender'
    
    gender_type = [
        ('female', female),
        ('male', male),
        ('select_gender', select_gender),
    ]

    gender= models.CharField(max_length=20, choices=gender_type, default= select_gender) 
    current_class = models.ForeignKey(Standard, on_delete=models.CASCADE, blank=True, null=True)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, blank=True, null=True)
    class_teacher = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, blank=True, null=True)
    badge =  models.ForeignKey(Badge, on_delete=models.CASCADE, blank=True, null=True, default='select')

    day_student = 'day_student'
    boarder = 'boarder'

    student_types = [
        (day_student, 'day_student'),
        (boarder, 'boarder'),

    ]

    student_type = models.CharField(max_length=15, choices=student_types, default=day_student)
    phone = models.CharField(max_length=15, blank=True) 
    address = models.CharField(max_length=120, blank=True)

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

    region_origin = models.CharField(max_length=20, choices=region_origin, default=select)

    date_admitted = models.DateField( verbose_name='Admission date (MM-DD-YYYY)')
    class_on_admission = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='studentdetails', verbose_name='class_on_admission') 
    
    # Guardian details here..
    guardian_name = models.CharField(max_length=60, blank=False)  
    guardian_address = models.TextField(max_length=120, blank=True)  
    guardian_phone = models.CharField(max_length=15, blank=True)
    guardian_email = models.CharField(max_length=30, blank=True)

    father = 'father'
    mother = 'mother'
    sister = 'sister'
    brother = 'brother'
    aunt = 'aunt'
    uncle = 'uncle'
    other = 'other'
    select = 'select'

    relationship = [
        (father, 'father'),
        (mother, 'mother'),
        (sister, 'sister'),
        (brother, 'brother'),
        (aunt, 'aunt'),
        (uncle, 'uncle'),
        (other, 'other'), 
        (select, 'select'), 

    ]

    relationship = models.CharField(max_length=25, choices=relationship, default=select)
    
    active = 'active'
    graduated = 'graduated'
    dropped = 'dropped'
    expelled = 'expelled'
    suspended = 'suspended'

    student_status = [
        (active, 'active'),
        (graduated, 'graduated'),
        (dropped, 'dropped'),
        (expelled, 'expelled'),
        (suspended, 'suspended'),

    ]

    student_status = models.CharField(max_length=15, choices=student_status, default=active)

    def __str__(self):
        return f'{self.last_name } - {self.first_name} ({self.user.username})'