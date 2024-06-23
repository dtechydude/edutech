from tkinter import Widget
from django import forms
from curriculum.models import Standard, ClassGroup, Session
from results.models import Examination, ExamSubject
from staff.models import StaffCategory, Department


class ClassRegisterForm(forms.ModelForm):

    class Meta:
        model = Standard
        fields = ('name', 'description',)

class ClassgroupRegisterForm(forms.ModelForm):

    class Meta:
        model = ClassGroup
        fields = ('name', 'description',)

class SessionRegisterForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('name', 'description',)

class CategoryRegisterForm(forms.ModelForm):

    class Meta:
        model = StaffCategory
        fields = ('name', 'description',)

class DepartmentRegisterForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name', 'description',)

class SubjectRegisterForm(forms.ModelForm):

    class Meta:
        model = ExamSubject
        fields = ( 'subject_id', 'name', 'description',)



class ExamRegisterForm(forms.ModelForm):

    class Meta:
        model = Examination
        fields = ('name', 'description', 'standard',)