from django.shortcuts import *
from django.urls import *
from . models import *
from . forms import *
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def customer_page(request):
    return render(request, 'customers/customers_page.html')

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

def assign(request, pk):   
    complaint = get_object_or_404(Complaint, id=pk)
    if request.method == 'POST':
        form = AssignForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.complaint = complaint
            form.save()
            messages.success(request, 'Operation was successfull')
            return redirect('complaint_detail', complaint.pk)
    else:
        form = AssignForm()
    return render(request, 'complaints/assign_form.html', {'form': form})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {
        'customers': customers
    })

def customer_details(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    complaints = Complaint.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'complaints': complaints
    }
    return render(request, 'customers/customer_details.html', context)

def get_session_data(request):
    return request.session.get('complaint', {})

def set_session_data(request, data):
    request.session['complaint'] = data

def clear_session_data(request):
    if 'complaint' in request.session:
        del request.session['complaint']

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():

            # Save name, email, and phone in session
            session_data = get_session_data(request)
            session_data['name'] = name
            session_data['email'] = email
            session_data['phone'] = phone
            
            session_data['name'] = customer.id
            set_session_data(request, session_data)
    
            return redirect('complaint_add')
    else:
        form = CustomerForm()

    return render(request, 'customers/customer_form.html', {'form': form})

def crime_step_three(request):
    # Retrieve session data from previous steps
    session_data = get_session_data(request)
    name = session_data.get('name')
    email = session_data.get('email')
    phone = session_data.get('phone')

    # Validate that session data exists
    if not name or not email or not phone:
        return redirect('customer_add')

    if request.method == 'POST':
        if form.is_valid():
            # Create and save the CrimeDetail instance
            complaint = form.save(commit=False)
            complaint.customer_id = customer_id
            crime_detail.month = month
            crime_detail.year = year
            crime_detail.save()

            messages.success(request, 'Data saved successfully')
            clear_session_data(request)  # Clear session after saving
            return redirect('base')  # Redirect to a success or base page

    return render(request, 'crime_details/crime_step_three.html', {
        'form': form,
        'station': station,
        'offence': offence,
        'month': month,
        'year': year,
    })


        
    