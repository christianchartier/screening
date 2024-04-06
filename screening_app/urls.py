from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('screening-recommendation/', views.screening_recommendation, name='screening_recommendation'),
]
