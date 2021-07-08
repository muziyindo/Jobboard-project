from django.db import models
from django.contrib.auth.models import User #added this

# Create your models here.

class Job_Position(models.Model):
	job_title = models.CharField(max_length=200)
	job_description =  models.TextField()
	job_expiry_date = models.DateField(auto_now=False, auto_now_add=False)
	employer_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.job_title


