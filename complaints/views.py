from django.shortcuts import *
from django.urls import *
from . models import *
from . forms import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def complaints_view(request):
    return render(request, 'complaints.html')

def complaints(request):
    complaints = Complaint.objects.all().order_by('-date_submitted')
    return render(request, 'complaints/complaints_list.html', {
        'complaints': complaints
    })

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, id=pk)
    complaints = Complaint.objects.all()
    context = {
        'complaint': complaint,
        'complaints': complaints,
    }
    return render(request, 'complaints/complaint_detail.html', context)