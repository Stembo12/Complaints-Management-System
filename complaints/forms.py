from django import forms
from .models import *
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, HTML
# from crispy_forms.bootstrap import Field

class AssignForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['assigned_to']
        
        labels = {
            'assigned_to': 'Assign'
        }