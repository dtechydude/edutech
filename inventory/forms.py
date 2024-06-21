from tkinter import Widget
from django import forms
from inventory.models import InventoryItems

class InventoryRegisterForm(forms.ModelForm):

    class Meta:
        model = InventoryItems
        fields = ('name', 'description', 'item_location', 'staff_in_charge', 'date_recorded',)
        
        widgets = {
            'date_recorded': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),

            
         }
