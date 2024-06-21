from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from quizes.models import Quiz


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'


