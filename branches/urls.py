from django.urls import path
from .views import *

urlpatterns = [
    path('branch/add/', branch_add, name='branch_add'),
    path('list/', branch_list, name='branch_list'),
    path('branch/<int:pk>/change', branch_update, name='branch_update'),
    path('branch/<int:pk>/delete', branch_delete, name='branch_delete'),
]