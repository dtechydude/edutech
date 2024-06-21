from .models import StaffProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_student(sender, instance, created, *args, **kwargs):
    if created:
        StudentDetail.objects.create()

@receiver(post_save, sender=User)
def save_studentdetail(sender, instance, **kwargs):
    instance.studentdetail.save()