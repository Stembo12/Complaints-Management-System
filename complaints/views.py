from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def complaints_view(request):
    return render(request, 'complaints.html')

def complaints(request):
    complaints = Complaint.objects.all().order_by('-date_submitted')
    context = {
        'complaints': complaints
    }
    return render(request, 'complaints/complaints_list.html', context)