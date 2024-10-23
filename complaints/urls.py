from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/page', views.customer_page, name='customers-page'),
    path('complaints/', views.complaints_view, name='complaints'),
    path('complaints/list', views.complaints, name='complaints_list'),
    path('complaint/<int:pk>/details/', views.complaint_detail, name='complaint_detail'),

    path('customers/', views.customers, name='customers_list'),
    path('customer/<int:pk>/details/', views.customer_details, name='customer_details'),
    
    path('complaint/<int:pk>/assign/', views.assign, name='assign')
]