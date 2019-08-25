from django import forms
from .models import Member

class MemberCreationForm(forms.ModelForm):
    """MemberCreationForm definition."""

    class Meta:

        model = Member

        fields = ('first_name', 'last_name','email', 'born', 'roll_no', 'image')
