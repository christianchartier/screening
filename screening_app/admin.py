from django.contrib import admin
from .models import ScreeningGuideline, ScreeningRule

@admin.register(ScreeningGuideline)
class ScreeningGuidelineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'notes', 'province', 'questions', 'rules')

@admin.register(ScreeningRule)
class ScreeningRuleAdmin(admin.ModelAdmin):
    list_display = ('guideline', 'min_age', 'max_age', 'gender', 'screening_test', 'interval_years', 'notes')
