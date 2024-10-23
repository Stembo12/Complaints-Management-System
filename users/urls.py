from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path
from .views import *
from . import views


urlpatterns = [

    
    path('users/list/', views.user_list, name='user_list'),
    path('user/<int:pk>/delete/', delete_user, name='user_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
    # recover passwrd
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password/reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password/confirm_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
    # # Change Password
    # # path('user/password/change/', change_password, name='change-password'),
    
    
    path('register/', register_user, name='user_add'),
    # # path('user/<str:pk>/profile/', UserProfile.as_view(), name='user-profile'),
    path('user/<str:pk>/update/', update_user, name='user_update'),
    
]

