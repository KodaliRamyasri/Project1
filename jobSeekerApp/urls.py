from django.urls import path
from . import views

urlpatterns = [
    path('jobDetailsList/', views.jobDetailsList, name='jobDetailsList'),
    path('applyToJob/<int:job_id>', views.applyToJob, name='applyToJob'),
    path('create/', views.jobProfileCreate, name='jobProfileCreate'),
    path('success/', views.jobProfileSuccess, name='jobProfileSuccess'),
    path('jobSearch/', views.jobSearch, name='jobSearch'),
]

