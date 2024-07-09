from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def addJobPost(request):
    return render(request,'employerApp/addJobPost.html')
def addJobPost1(request):
    if request.method == "POST":
        jobID = request.POST['jobID']
        jobTitle = request.POST['jobTitle']
        skills = request.POST['skills']
        experience = request.POST['experience']
        salary = request.POST['salary']
        location = request.POST['location']
        data = jobPost(jobID=jobID,jobTitle=jobTitle,skills=skills,experience=experience,salary=salary,location=location)
        data.save()
        return HttpResponse("<h1><center>Thank you for submitting the application</center></h1>")
    else:
        HttpResponse("<h1>Error</h1>")

def viewJobDetails(request):
    jobDetailsList=jobPost.objects.all()
    return render(request,'employerApp/viewJobDetails.html',{'jobDetailsList':jobDetailsList})

from django.contrib import messages
from .models import jobPost

def deleteJobDetails(request, job_id):
    job = get_object_or_404(jobPost, id=job_id)

    if request.method == "POST":
        job.delete()
        messages.success(request, 'Job deleted successfully.')
        return redirect('viewJobDetails')

    return render(request, 'employerApp/delete.html', {'job': job})

def editJobDetails(request, job_id):
    jobDetails = get_object_or_404(jobPost, id=job_id)
    if request.method == 'POST':
        jobDetails.jobTitle= request.POST.get('jobTitle')
        jobDetails.jobID = request.POST.get('jobID')
        jobDetails.salary = request.POST.get('salary')
        jobDetails.experience = request.POST.get('experience')
        jobDetails.location = request.POST.get('location')
        jobDetails.skills = request.POST.get('skills')
        jobDetails.save()
        return redirect('viewJobDetails')
    return render(request, 'employerApp/editJobDetails.html', {'jobDetails':jobDetails})

from jobSeekerApp.models import jobApplication
def jobApplicationList(request):
    jobApplications=jobApplication.objects.all()
    return render(request,'employerApp/jobApplicationList.html',{'jobApplications':jobApplications})