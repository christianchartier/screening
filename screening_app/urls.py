from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('screening-recommendation/<int:guideline_id>/', views.screening_recommendation, name='screening_recommendation'),
]
