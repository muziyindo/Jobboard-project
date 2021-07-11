from django import forms
from django.forms.widgets import NumberInput #for the date field

CATEGORIES = [
	('finance','Finance'),
	('engineering','Engineering'),
	('engineering','Sales/Marketing'),

]

class JobPostForm(forms.Form):
	employer_email = forms.EmailField(required = True, label = "Your Email")
	title = forms.CharField(required = True, label = "Job Title")
	location = forms.CharField(required = True, label = "Job Location")
	category = forms.ChoiceField(choices=CATEGORIES, required = True, label = "Job Category")
	description = forms.CharField(widget=forms.Textarea, required = True, label = "Job description")
	application_email_website = forms.CharField(required = True, label = "Email or Website for Application")
	closing_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required = True, label = "Job Expiry Date")
	company_name = forms.CharField(required = True, label = "Company Name")
	company_website = forms.CharField(required = False, label = "Company Website")