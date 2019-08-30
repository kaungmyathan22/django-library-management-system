from django import forms
from .models import Issue

class IssueAddForm(forms.ModelForm):

    class Meta:
        
        model = Issue

        exclude = ["return_date"]