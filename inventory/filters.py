import django_filters
from .models import InventoryItems
from django.contrib.auth.models import User

class InventoryFilter(django_filters.FilterSet):

    class Meta:
        model = InventoryItems
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'name', 'staff_in_charge', 'item_location'}
        

