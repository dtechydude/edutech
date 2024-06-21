from django.contrib import admin
from inventory.models import InventoryItems

# Register your models here.
class InventoryItemsAdmin(admin.ModelAdmin):
    
    list_display=('name', 'item_location', 'staff_in_charge', 'date_recorded',)
    

admin.site.register(InventoryItems, InventoryItemsAdmin)

