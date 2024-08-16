from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from curriculum.models import Standard, ClassGroup
from django.urls import reverse
from staff.models import StaffProfile

class Badge(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__ (self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StudentDetail(models.Model):
    student_username = models.CharField(max_length=20, unique=True, verbose_name='Student ID', help_text='Type New Username For Student')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Student Username', help_text='Click The Search Button To Select The New Username')
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(blank=True, null=True, verbose_name='Date of Birth(Y-M-D)', default='2020-01-01')

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
    badge =  models.ForeignKey(Badge, on_delete=models.CASCADE, blank=True, null=True, default='not a prefect', verbose_name='Prefect Tittle (if is prefect)')

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

    date_admitted = models.DateField(default='2020-01-01')
    class_on_admission = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='studentdetails', verbose_name='class_on_admission') 
    
    # Guardian details here..
    guardian_name = models.CharField(max_length=60, blank=False)  
    guardian_address = models.TextField(max_length=120, blank=True)  
    guardian_phone = models.CharField(max_length=15, blank=True)
    guardian_email = models.CharField(max_length=30, blank=True)

    select = 'select'
    father = 'father'
    mother = 'mother'
    sister = 'sister'
    brother = 'brother'
    aunt = 'aunt'
    uncle = 'uncle'
    other = 'other'
    

    relationship = [
        (select, 'select'),
        (father, 'father'),
        (mother, 'mother'),
        (sister, 'sister'),
        (brother, 'brother'),
        (aunt, 'aunt'),
        (uncle, 'uncle'),
        (other, 'other'), 
         

    ]

    relationship = models.CharField(max_length=25, choices=relationship, default=select, help_text="Guardian's Relationship With Student")
    
    active = 'active'
    inactive = 'inactive'
    graduated = 'graduated'
    dropped = 'dropped'
    expelled = 'expelled'
    suspended = 'suspended'

    student_status = [
        (active, 'active'),
        (inactive, 'inactive'),
        (graduated, 'graduated'),
        (dropped, 'dropped'),
        (expelled, 'expelled'),
        (suspended, 'suspended'),

    ]

    student_status = models.CharField(max_length=15, choices=student_status, default=inactive)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'{self.last_name } - {self.first_name} ({self.user.username}) {self.current_class}'
    
    def get_absolute_url(self):
        return reverse('students:students-detail', kwargs={'id':self.id})
    
    # def save(self, *args, **kwargs):
    #     if self.student_username == "":
    #         student_username=self.user
    #         self.student_username = student_username
    #         super().save(*args, **kwargs)