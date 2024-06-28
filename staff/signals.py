from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import StaffProfile


@receiver(post_save, sender=User)
def post_save_create_staff(sender, instance, created, *args, **kwargs):
    if created:
        StaffProfile.objects.create()

@receiver(post_save, sender=User)
def save_staffprofile(sender, instance, **kwargs):
    instance.staffprofile.save()