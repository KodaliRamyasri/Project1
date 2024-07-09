from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
# Create your views here.
from employerApp.models import jobPost
from django.contrib.auth.decorators import login_required
#@login_required(login_url='logIn')
def jobDetailsList(request):
    jobDetailsList=jobPost.objects.all()
    return render(request,'jobSeekerApp/viewJobs.html',{'jobDetailsList':jobDetailsList})

def applyToJob(request,job_id):
    jobDetails = get_object_or_404(jobPost, id=job_id)
    if request.method == 'POST':
        form = jobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            jobApplication = form.save(commit=False)
            jobApplication.jobDetails = jobDetails
            jobApplication.save()

            subject = 'Job Application Received'
            message = 'Thank you for applying to the Job. Your application is received and will be sent to next process'
            from_email = 'kodaliramyasri54@gmail.com'
            recipient_list = [jobApplication.email]
            send_mail(subject, message, from_email, recipient_list)
        return redirect('jobDetailsList')
    else:
        form = jobApplicationForm()

    return render(request, 'jobSeekerApp/applyToJob.html', {'jobDetails': jobDetails, 'form': form})

from django.shortcuts import render, redirect
from .forms import JobProfileForm

def jobProfileCreate(request):
    if request.method == 'POST':
        form = JobProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobProfileSuccess')  # Assuming you have a success URL
    else:
        form = JobProfileForm()
    return render(request, 'jobSeekerApp/jobSeekerProfile.html', {'form': form})

def jobProfileSuccess(request):
    return render(request, 'jobSeekerApp/jobProfileSuccess.html')

def jobSearch(request):
    query = request.GET.get('q')
    query1=request.GET.get('r')
    if query and query1:
        jobDetailsList = jobPost.objects.filter(jobTitle__icontains=query,location__icontains=query1)
    elif query:
        jobDetailsList = jobPost.objects.filter(jobTitle__icontains=query)
    elif query1:
        jobDetailsList = jobPost.objects.filter(location__icontains=query1)
    else:
        jobDetailsList = jobPost.objects.all()

    noMatch=not jobDetailsList.exists()
    context = {'jobDetailsList': jobDetailsList,'noMatch': noMatch}
    return render(request, 'jobSeekerApp/viewJobs.html', context)
