from django import forms
from.models import Notifications, SchoolCalendar, NotificationStudent



class MailForm(forms.ModelForm):
   
    class Meta:
        
        model = Notifications
        fields = ('student', 'staff', 'subject', 'content', 'attachement')

class StudentMailForm(forms.ModelForm):
   
    class Meta:
        
        model = NotificationStudent
        fields = ('subject', 'content')


# class ReplyMailForm(forms.ModelForm):
#     class Meta:
#         model = ReplyMailForm
#         fields = ('reply_body',)

#         widgets = {
#             'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),

class EventRegisterForm(forms.ModelForm):
   
    class Meta:
        
        model = SchoolCalendar
        fields = ('event_name', 'event_description', 'event_date', 'duration',)

class EventUpdateForm(forms.ModelForm):
   
    class Meta:
        
        model = SchoolCalendar
        fields = ('event_name', 'event_description', 'event_date', 'duration',)