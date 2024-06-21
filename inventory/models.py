from django.db import models
from staff.models import StaffProfile

# Create your models here.


class InventoryItems(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=150, blank=True)
    item_location = models.CharField(max_length=150, blank=True)
    staff_in_charge = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, blank=True, null=True )
    date_recorded = models.DateField(default=None)
    date_added = models.DateField(auto_now=True)


    def __str__ (self):    
        return f'{self.name}'

    class Meta:
        verbose_name = 'Inventory Items'
        verbose_name_plural = 'Inventory Items'
