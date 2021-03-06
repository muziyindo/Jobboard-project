from django.shortcuts import render, redirect
from django.http import HttpResponse
#import re # for email validation
from .models import Job
from .forms import JobPostForm #imported this for the post job form

# Create your views here.

def home(request):
	jobs = Job.objects.all()
	return render(request, 'home.html',{'jobs':jobs})

def jobs(request):
	return HttpResponse('Jobs')

def post_job(request):
	
	if request.method == 'POST':

		#using django modelform and its validation
		form = JobPostForm(request.POST)
		if form.is_valid():
			job = Job()
			job.employer_email = form.cleaned_data['employer_email']
			job.title = form.cleaned_data['title']
			job.location = form.cleaned_data['location']
			job.category = form.cleaned_data['category']
			job.job_type = form.cleaned_data['job_type']
			job.description = form.cleaned_data['description']
			job.application_email_website = form.cleaned_data['application_email_website']
			job.closing_Date = form.cleaned_data['closing_Date']
			job.company_name = form.cleaned_data['company_name']
			job.company_website = form.cleaned_data['company_website']
			job.save()
			return redirect('/')
		else:
			print(form.errors)

	else:
		form = JobPostForm()
	return render(request, 'Job/post_job.html',{'page_title':'Post a Job','form':form})


	#manual email validation
	#error_message = []
	#regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	'''
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
	if bool(request.POST['job_type'])== False :
		error_message.append('Job Type Field is required')
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
		job.employer_email = form.cleaned_data['employer_email']
		job.title = form.cleaned_data['title']
		job.location = form.cleaned_data['location']
		job.category = form.cleaned_data['category']
		job.job_type = form.cleaned_data['job_type']
		job.description = form.cleaned_data['description']
		job.application_email_website = form.cleaned_data['application_email_website']
		job.closing_Date = form.cleaned_data['closing_Date']
		job.company_name = form.cleaned_data['company_name']
		job.company_website = form.cleaned_data['company_website']
		job.save()

		return render(request, 'Job/post_job.html',{'message':'success'})'''


	

