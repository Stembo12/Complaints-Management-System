from django.shortcuts import *
from django.contrib import messages
from . forms import *

# Create your views here.
def branch_add(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Branch added successfully.')
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'branches/branch_form.html', {'form': form})

def branch_update(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Branch updated successfully.')
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'branches/branch_form.html', {'form': form}) 

def branch_delete(request, pk):
    branch = get_object_or_404(Branch, id=pk)
    if request.method == 'POST':
        branch.delete()
        messages.success(request, 'Branch deleted successfully.')
        return redirect('branch_list')
    return render(request, 'confirm_delete.html', {'branch': branch}) 
        

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branches': branches}) 