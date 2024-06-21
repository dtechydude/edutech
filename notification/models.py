from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from students.models import StudentDetail
from staff.models import StaffProfile

# Create your models here.

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ManyToManyField(StudentDetail, related_name='student_mail', blank=True)
    staff = models.ManyToManyField(StaffProfile, related_name='staff_mail', blank=True)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    attachement = models.FileField(upload_to='attachement', blank=True, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('notification:mail-self')


class Notifications(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ManyToManyField(StudentDetail, related_name='mail_student', blank=True)
    staff = models.ManyToManyField(StaffProfile, related_name='mail_staff', blank=True)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    attachement = models.FileField(upload_to='attachement', blank=True, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('notification:mail-self')

    class Meta:
        verbose_name = 'Send Notification Message'
        verbose_name_plural = 'Send Notification Message'


class NotificationStudent(models.Model):
    sender = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('notification:student-mail')

    class Meta:
        verbose_name = 'Received Students Messages'
        verbose_name_plural = 'Received Students Messages'



class NotificationStudents(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_recipients', blank=True, null=True)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('notification:student-mail')



class MailReply(models.Model):
    notification_name = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.sender.sender)


class SchoolCalendar(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_date = models.DateField()
    duration = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.event_name} - {self.event_date}'