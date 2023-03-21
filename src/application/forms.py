from django import forms
from .models import Application

class ApplicationCreationForm(forms.ModelForm):
    name = forms.CharField(label='Please enter your first and last name')
    email = forms.CharField(label='Please enter your bc.edu email')
    eagleID = forms.IntegerField(label='Please enter your 8-digit Eagle ID')
    courseHistory = forms.CharField(label='Have you taken this course and if so what grade did you receive?')
    interest = forms.CharField(label='Why are you interested in being a TA for this course?')
    experience = forms.CharField(label='Please explain any relevant experience you have with course material')
    