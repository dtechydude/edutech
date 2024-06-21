from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from inventory.models import InventoryItems
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from inventory.forms import InventoryRegisterForm

from .filters import InventoryFilter
from django_filters.views import FilterView
# For panigation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# for csv
import csv

# Create your views here.


class InventoryListView(LoginRequiredMixin, ListView):
    context_object_name = 'inventory'
    model = InventoryItems
    # template_name = 'curriculum/class_list.html'
    template_name = 'inventory/inventory_items.html'


@login_required
def inventory_register_form(request):
    if request.method == 'POST':
        
        inventory_form = InventoryRegisterForm(request.POST)
        if inventory_form.is_valid():
           
            inventory_form.save()
            messages.success(request, f'New Inventory item Registered successfully, Register another or go to inventory list')
            return redirect('inventory:inventory_items')
    else:
      
        inventory_form = InventoryRegisterForm

    context = {
        
        'inventory_form': inventory_form,
    }

    return render(request, 'inventory/inventory_register.html', context)


@login_required
def inventory_list(request):
    inventory_list = InventoryItems.objects.all()
    inventory_filter = InventoryFilter(request.GET, queryset=inventory_list) 
    inventory_list = inventory_filter.qs
    
    # PAGINATOR METHOD
    page = request.GET.get('page', 1)
    paginator = Paginator(inventory_list, 10)
    try:
        inventory_list = paginator.page(page)
    except PageNotAnInteger:
        inventory_list = paginator.page(1)
    except EmptyPage:
        inventory_list = paginator.page(paginator.num_pages)

    context = {
        'inventory_list' : InventoryItems.objects.all(),
        'inventory_filter': inventory_filter,
        'inventory_list': inventory_list

    }
    return render (request, 'inventory/inventory_items.html', context)


# Generate a CSV inventory list
def inventory_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=inventory.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    inventory = InventoryItems.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['INVENTORY NAME', 'DESCRIPTION', 'LOCATION', 'DATE ADDED', 'STAFF IN CHARGE',])


    # Loop thru and output
    for item in inventory:
        writer.writerow([item.name, item.description, item.item_location, item.date_recorded, item.staff_in_charge,])
        
    return response