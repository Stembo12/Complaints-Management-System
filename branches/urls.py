from django.urls import path
from .views import *

urlpatterns = [
    path('branch/add', branch_add, name='branch_add'),
]