from django.shortcuts import render
from .models import ScreeningGuideline, ScreeningRule
from .forms import PatientForm

def home(request):
    guidelines = ScreeningGuideline.objects.all()
    return render(request, 'home.html', {'guidelines': guidelines})
def screening_recommendation(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            province = form.cleaned_data['province']
            rules = ScreeningRule.objects.filter(
                guideline__province=province,
                min_age__lte=age,
                max_age__gte=age,
                gender=gender
            )
            return render(request, 'recommendation.html', {'rules': rules})
    else:
        form = PatientForm()
    return render(request, 'screening_form.html', {'form': form})
