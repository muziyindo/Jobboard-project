from django.db import models
from django.contrib.auth.models import User #added this

# Create your models here.
class Job(models.Model):
	employer_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
	employer_email = models.CharField(max_length=200)
	title = models.CharField(max_length=300)
	location = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	description = models.TextField()
	application_email_website = models.CharField(max_length=255)
	closing_Date = models.DateField(auto_now_add=True)
	company_name = models.CharField(max_length=200)
	company_website = models.CharField(max_length=200)

	def __str__(self):	
		return self.company_name