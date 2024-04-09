from django import forms
from .models import ScreeningGuideline, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        guideline_id = kwargs.pop('guideline_id', None)
        super().__init__(*args, **kwargs)
        if guideline_id:
            guideline = ScreeningGuideline.objects.get(id=guideline_id)
            for question in guideline.questions:
                self.fields[question] = forms.ChoiceField(
                    choices=[(True, 'Yes'), (False, 'No')],
                    widget=forms.RadioSelect,
                    label=question,
                    required=True
                )