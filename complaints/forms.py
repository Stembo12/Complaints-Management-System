from django import forms
from .models import *
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, HTML
# from crispy_forms.bootstrap import Field

class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ['staff']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_type', 'details', 'branch']
        