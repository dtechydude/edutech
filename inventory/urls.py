from django.urls import path
from . import views
from inventory import views as inventory_views



app_name = 'inventory'

urlpatterns = [
    # path('', views.InventoryItems.as_view(), name='inventory_items'),
    # path('', views.InventoryListView.as_view(), name='inventory_items'),
    path('', inventory_views.inventory_list, name="inventory_items"),
    path('inventory-form/', inventory_views.inventory_register_form, name="inventory_form"),
    path('inventory-csv', inventory_views.inventory_csv, name="inventory-csv"),

]