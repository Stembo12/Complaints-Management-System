from django import forms
from .models import *
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, HTML
# from crispy_forms.bootstrap import Field

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'