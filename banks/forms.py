from django import forms
from .models import Bank, Branch
# name, description, inst_num, swift_code

class bankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'swift_code', 'institution_number', 'description']
    # name = forms.CharField(max_length=100)
    # swift_code = forms.CharField(max_length=100)
    # institution_number = forms.CharField(max_length=100)
    # description = forms.CharField(max_length=100)