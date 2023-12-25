from django import forms
from .models import Bank, Branch
# name, description, inst_num, swift_code

class bankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'swift_code', 'institution_number', 'description']