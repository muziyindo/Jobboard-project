from django.shortcuts import render, redirect
from django.http import HttpResponse
import re # for email validation
from .models import Job
#from .forms import JobPostForm #imported this for the post job form

# Create your views here.

def home(request):
	return render(request, 'home.html')

def jobs(request):
	return HttpResponse('Jobs')

def post_job(request):
	error_message = []
	if request.method == 'POST':

		#email validation
		regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		if bool(request.POST['employer_email'])== False :
			error_message.append('Email Field is required')
		elif bool(re.match(regex, request.POST['employer_email']))== False :
			error_message.append('Email entered is invalid')
		if bool(request.POST['title'])== False :
			error_message.append('Job title Field is required')
		if bool(request.POST['location'])== False :
			error_message.append('Job Location Field is required')
		if bool(request.POST['category'])== False :
			error_message.append('Job category Field is required')
		if bool(request.POST['description'])== False :
			error_message.append('Job description Field is required')
		if bool(request.POST['application_email_website'])== False :
			error_message.append('Application email/URL Field is required')
		if bool(request.POST['closing_Date'])== False :
			error_message.append('closing_Date Field is required')
		if bool(request.POST['company_name'])== False :
			error_message.append('company_name Field is required')



		#if there is an error from the validation above
		if bool(error_message) == True :
			return render(request, 'Job/post_job.html',{'error':error_message})
		else:
			job = Job()
			job.employer_email = request.POST['employer_email']
			job.title = request.POST['title']
			job.location = request.POST['location']
			job.category = request.POST['category']
			job.description = request.POST['description']
			job.application_email_website = request.POST['application_email_website']
			job.closing_Date = request.POST['closing_Date']
			job.company_name = request.POST['company_name']
			job.company_website = request.POST['company_name']
			job.save()

			return render(request, 'Job/post_job.html',{'message':'success'})

	else:
		return render(request, 'Job/post_job.html',{'page_title':'Post a Job'})