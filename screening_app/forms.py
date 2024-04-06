from django import forms
from .models import ScreeningGuideline

class PatientForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    province = forms.ChoiceField(
        choices=ScreeningGuideline.PROVINCE_CHOICES,
        initial='QC'  # Set the default value to 'QC' for Quebec
    )
