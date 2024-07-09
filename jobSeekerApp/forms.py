from django import forms
from .models import *

class jobApplicationForm(forms.ModelForm):
    class Meta:
        model=jobApplication
        fields=['name','email','resume','coverLetter']
    def __init__(self,*args,**kwargs):
        super(jobApplicationForm,self).__init__(*args,**kwargs)

from django import forms
from .models import JobProfile

class JobProfileForm(forms.ModelForm):
    class Meta:
        model = JobProfile
        fields = ['name', 'email', 'gender', 'education', 'job_type', 'experience', 'skills', 'summary', 'profile_picture']
