from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def projectHomePage(request):
    return render(request,'adminApp/projectHomePage.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='projectHomePage')
def employerHomePage(request):
    return render(request,'employerApp/employerHomePage.html')

@login_required(login_url='projectHomePage')
def jobSeekerHomePage(request):
    return render(request, 'jobSeekerApp/jobSeekerHomePage.html')
def print1(request):
    return render(request,'adminApp/printToConsole.html')
def printToConsole(request):
    if request.method=="POST":
        userInput=request.POST['userInput']
        print(f'User input: {userInput}')
    a1= {'userInput':userInput}
    return render(request,'adminApp/printToConsole.html',a1)
def add1(request):
    return render(request,'adminApp/additionExample.html')
def add(request):
    if request.method=="POST":
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        sum = num1 + num2
    a1= {'sum':sum}
    return render(request,'adminApp/additionExample.html',a1)

import random
import string
def randomPageCall(request):
    return render(request,'adminApp/randomExample.html')

def randomLogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1={'ran':ran}
    return render(request, 'adminApp/randomExample.html',a1)

from .forms import *
from datetime import timedelta
def getDatePageCall(request):
    return render(request, 'adminApp/getDate.html')

def getDateLogic(request):
    if request.method=="POST":
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+timedelta(days=integer_value)
            return render(request,'adminApp/getdate.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'adminApp/getDate.html',{'form':form})

from .forms import *
from datetime import datetime
import pytz
def location_time(request):
    return render(request,'adminApp/locationTime.html')

# views.py
from django.shortcuts import render
from datetime import datetime
import pytz
from .forms import LocationForm

def location_time_view(request):
    current_time = None
    selected_location = None

    if request.method == 'POST':
        form = LocationForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            selected_location = form.cleaned_data['timezone']
            timezone = pytz.timezone(selected_location)
            current_time = datetime.now(timezone)
            print(f"Selected Location: {selected_location}")
            print(f"Current Time: {current_time}")
    else:
        form = LocationForm()  # If GET request or initial form display

    context = {
        'form': form,
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S') if current_time else None,
        'selected_location': selected_location,
    }
    print("Context Data:", context)
    return render(request, 'adminApp/locationTime.html', context)

def signIn(request):
    return render(request,'adminApp/signIn.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth
def signIn1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already Taken.')
                return render(request,'adminApp/signIn.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!')
                return render(request,'adminApp/projectHomePage.html')
        else:
            messages.info(request,'Password does not match.')
            return render(request,'adminApp/signIn.html')
def contactPageCall(request):
    return render(request, 'adminApp/contact.html')

def contactLogic(request):
    if request.method=="POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        comment = request.POST['comment']
        data=contactUs(firstName=firstName,lastName=lastName,email=email,comment=comment)
        data.save()
        subject = 'Thank you for your valuable feedback'
        send_mail(
            subject,
            comment,
            'kodaliramyasri54@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Thank you for giving the Feedback</center></h1>")
    else:
        HttpResponse("<h1>Error</h1>")

def logIn(request):
    return render(request,'adminApp/logIn.html')

def logIn1(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                return redirect('jobSeekerHomePage')
            elif len(username)==4:
                return redirect('employerHomePage')
            else:
                return redirect('projectHomePage')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'adminApp/logIn.html')
    else:
        return render(request,'adminApp/logIn.html')

def logOut(request):
    auth.logout(request)
    return redirect('projectHomePage')

import requests

def weatherPageCall(request):
    return render(request, 'adminApp/weatherApp.html')

def weatherLogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'adminApp/weatherApp.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'adminApp/weatherApp.html', {'error_message': error_message})

import csv
from django.core.mail import send_mail
def sendEmails(request):
    csvFilePath=r'C:\PFSD\pythonProject\djangoProject\KLJobPortal\static\csv\mailFile.csv'
    with open(csvFilePath,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            recipientEmail=row['MAIL']
            subject='Hello KLUian'
            messageBody='Hey, Welcome to PFSD Class, Hope you have a great day!!'
            send_mail(
                subject,
                messageBody,
                'kodaliramyasri54@gmail.com',
                [recipientEmail],
                fail_silently=False,
            )
            print(f'Sent email to{recipientEmail}')
    return render(request,'adminApp/emailSent.html')

def qrPageCall(request):
    return render(request,'adminApp/qrPageCall.html')

import qrcode
from django.conf import settings
import os
def qrLogic(request):
    if request.method=="POST":
        userInput=request.POST['userInput']
        print(f'User input:{userInput}')
        data=userInput
        qr=qrcode.QRCode(version=1,box_size=20,border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        img_path=os.path.join(settings.STATICFILES_DIRS[0],'KLU1.png')
        img.save(img_path)
    return render(request, 'adminApp/qrPageCall.html',{'img_path':'KLU1.png'})