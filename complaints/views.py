from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def complaints_view(request):
    return render(request, 'complaints.html')
