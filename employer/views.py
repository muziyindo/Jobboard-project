from django.shortcuts import render
from .models import Job_Position

# Create your views here.

def jobs(request):
	job_positions = Job_Position.objects.all()
	return render(request, 'home.html',{'job_positions':job_positions})
