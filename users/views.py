from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from users.models import *
from django.views.generic.edit import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from users.forms import *

# Create your views here.
   
@login_required
def user_list(request):
    users = Staff.objects.all()
    return render(request, 'users/users_list.html', {'users': users})

@login_required
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Return success message for registration
            messages.success(request, 'User registered successfully!')
            return redirect('user_list')
    else:
        form = RegisterForm()
    # Render the form for GET request
    return render(request, 'users/user_form.html', {'form': form})

@login_required
def update_user(request, pk):
    user = get_object_or_404(Staff, id=pk)
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user)      
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')                 
    else:
        form = UpdateUser(instance = user)
    return render(request, 'users/user_form.html', {'form': form})


@login_required
def delete_user(request, pk):
    user = get_object_or_404(Staff, id=pk)
    
    if request.method == 'POST':
        if not user.is_active:  # Check if the user is deactivated
            user.delete()
            messages.success(request, 'User deleted successfully!')
            return redirect('user_list')
        else:
            messages.error(request, 'User cannot be deleted. Deactivate the account first')
            # Redirect back to the user list or the same delete page for better UX
            return redirect('user_list')  # You can redirect elsewhere if needed

    return render(request, 'users/delete_user.html', {'user': user})


# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'User deleted successfully!')
#             return redirect('user_list')
#     else:
#         form = PasswordChangeForm(user=request.user)
#     return render(request, 'users/change_password.html', {'form': form})

    
# def user_profile(request, pk):
#     user = get_object_or_404(User, id=pk)
#     context = {
#         'user': user
#     }
#     return render(request, 'users/user_profile.html', context)

# def update_profile(request):
#     form = ProfileForm(request.POST, instance = request.user)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Changes saved successfully')
#             return render(request.META.get('HTTP_REFERER'))
#     else:
#         form = ProfileForm(request.POST, instance = request.user)
#     return render(request, 'users/user_form.html', {'form': form})

# class UserProfile(UpdateView, LoginRequiredMixin):
#     model = User
#     form_class = ProfileForm
#     template_name = 'users/user_profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["action"] = 'Update'
#         return context
    
#     def form_valid(self, form):
#         messages.success(self.request, 'Changes saved successfully')
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse('base')

    
    

