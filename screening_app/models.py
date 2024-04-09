from django.db import models

PROVINCE_CHOICES = [
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NL', 'Newfoundland and Labrador'),
    ('NS', 'Nova Scotia'),
    ('NT', 'Northwest Territories'),
    ('NU', 'Nunavut'),
    ('ON', 'Ontario'),
    ('PE', 'Prince Edward Island'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewan'),
    ('YT', 'Yukon'),
]

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='QC')
    
    def __str__(self):
        return self.name

class ScreeningGuideline(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    notes = models.TextField(blank=True)
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='QC')
    questions = models.JSONField(default=list)
    rules = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name

class ScreeningRule(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    guideline = models.ForeignKey(ScreeningGuideline, on_delete=models.CASCADE)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    screening_test = models.CharField(max_length=255)
    interval_years = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.guideline.name} - {self.screening_test}"
    
class PatientAnswer(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.BooleanField()
    
    def __str__(self):
        return f"{self.patient} - {self.question}: {self.answer}"
