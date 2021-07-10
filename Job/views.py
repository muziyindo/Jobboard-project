from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'home.html')

def jobs(request):
	return HttpResponse('Jobs')

def post_job(request):
	context = {
		'page_title':'Post a Job'
	}
	return render(request, 'Job/post_job.html',context)
