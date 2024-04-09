from django.shortcuts import render, redirect
from .models import ScreeningGuideline, ScreeningRule, PatientAnswer, Patient, PROVINCE_CHOICES
from .forms import PatientForm

def home(request):
    guidelines = ScreeningGuideline.objects.all()
    return render(request, 'home.html', {'guidelines': guidelines})

def screening_recommendation(request, guideline_id):
    guideline = ScreeningGuideline.objects.get(id=guideline_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, guideline_id=guideline_id)
        if form.is_valid():
            patient = Patient.objects.create(
                name=request.POST['name'],
                age=request.POST['age'],
                gender=request.POST['gender'],
                province=request.POST['province']
            )
            patient_answers = []
            for question in guideline.questions:
                answer = form.cleaned_data.get(question)
                patient_answers.append(PatientAnswer(patient=patient, question=question, answer=answer))
            PatientAnswer.objects.bulk_create(patient_answers)
            recommendation = get_recommendation(patient, guideline)
            return render(request, 'recommendation.html', {'recommendation': recommendation})
    else:
        form = PatientForm(guideline_id=guideline_id)
    return render(request, 'screening_form.html', {'form': form, 'province_choices': PROVINCE_CHOICES})

def get_recommendation(patient, guideline):
    patient_answers = PatientAnswer.objects.filter(patient=patient)
    answers = {answer.question: answer.answer for answer in patient_answers}
    
    for rule in guideline.rules:
        conditions = rule['conditions']
        recommendation = rule['recommendation']
        
        if all(answers.get(condition['question']) == condition['answer'] for condition in conditions):
            return recommendation
    
    return "No recommendation found based on the provided answers."