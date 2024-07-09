from django.db import models

# Create your models here.
from employerApp.models import jobPost
class jobApplication(models.Model):
    jobDetails=models.ForeignKey(jobPost,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    resume=models.FileField(upload_to='resumes/')
    coverLetter=models.TextField()
    def __str__(self):
        return f"{self:name} {self:jobDetails}"

from django.db import models

class JobProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    EDUCATION_CHOICES = [
        ('highschool', 'High School'),
        ('bachelor', 'Bachelor\'s Degree'),
        ('master', 'Master\'s Degree'),
        ('phd', 'Ph.D.'),
    ]

    JOB_TYPE_CHOICES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    experience = models.IntegerField()
    skills = models.CharField(max_length=200)
    summary = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.name
