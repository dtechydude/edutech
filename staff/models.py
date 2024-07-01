from email.policy import default
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from curriculum.models import Standard, ClassGroup
from django.template.defaultfilters import slugify

import datetime


class StaffCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Staff Category'
        verbose_name_plural = 'Staff Categories'

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class StaffProfile(models.Model):
    staff_username = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True)
    female = 'female'
    male = 'male'
    select_gender = 'select_gender'
       
    gender_type = [
        ('female', female),
        ('male', male),
        ('select_gender', select_gender),
    ]

    gender= models.CharField(max_length=20, choices=gender_type, default=select_gender)
    address = models.CharField(max_length=200, blank=True, null=True)

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
    cat_name = models.ForeignKey(StaffCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    class_in_charge = models.ForeignKey(Standard, on_delete=models.SET_DEFAULT, default='no teacher', blank=True, null=True)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, blank=True, null=True)
    date_employed = models.DateField()

    married = 'married'
    single = 'single'
    select = 'select'

    marital_status = [
        (married, 'married'),
        (single, 'single'),
        (select, 'select'),
    ]

    marital_status = models.CharField(max_length=15, choices=marital_status, default=select)
    phone_home = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)

    # Academic information
    qualification = models.CharField(max_length=150)  
    year = models.DateField()   
    institution = models.CharField(max_length=150, blank=True)
    professional_body = models.CharField(max_length=150, blank=True)  
   
    # Guarantor's information
    guarantor_name = models.CharField(max_length=150, blank=True) 
    guarantor_phone = models.CharField(max_length=150, blank=True) 
    guarantor_address = models.CharField(max_length=150, blank=True) 
    guarantor_email = models.CharField(max_length=60, blank=True)
    
    # next of kin info
    next_of_kin_name = models.CharField(max_length=60, blank=True)  
    next_of_kin_address = models.CharField(max_length=150, blank=True)  
    next_of_kin_phone = models.CharField(max_length=15, blank=True) 

    form_teacher = 'form_teacher'
    principal = 'principal'
    head_teacher = 'head_teacher'
    admin_officer = 'admin_officer'
    account_officer = 'account_officer'
    non_teaching = 'non_teaching'
    others = 'others'
    select = 'select'

    
    staff_role = [
        ('form_teacher', form_teacher),
        ('principal', principal),
        ('head_teacher', head_teacher),
        ('admin_officer', admin_officer),
        ('account_officer', account_officer),
        ('non_teaching', non_teaching),
        ('others', others),
        ('select', select),
            
    ]
    staff_role= models.CharField(max_length=20, choices=staff_role, default=select)

    @property
    def is_teacher(self):
        if hasattr(self, 'user'):
            return True
        return False

    class Meta:
        ordering = ['user']


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        # return f'{self.staff_username}'
        return f'{self.user.username} - {self.last_name }  {self.first_name}'


    def get_absolute_url(self):
        return reverse('staff:staff_detail', kwargs={'id':self.id})
