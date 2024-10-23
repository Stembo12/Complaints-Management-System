from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complaints/', views.complaints_view, name='complaints'),
    path('complaints/list', views.complaints, name='complaints_list'),
    path('complaint/<int:pk>/view/', views.complaint_detail, name='complaint_detail'),

]