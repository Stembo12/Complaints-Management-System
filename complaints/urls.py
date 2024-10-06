from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complaints/', views.complaints_view, name='complaints'),
    path('complaints/list', views.complaints, name='complaints_list'),

]