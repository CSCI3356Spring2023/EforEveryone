from django import forms
from .models import Application

class ApplicationCreationForm(forms.ModelForm):
    email = forms.CharField(label='Please enter your bc.edu email')
    eagleID = forms.IntegerField(label='Please enter your 8-digit Eagle ID')
    cohort = forms.ChoiceField(choices=Application.COHORT_CHOICES, label='Select your class year')
    relation = forms.ChoiceField(choices=Application.RELATION_CHOICES, label='Select your relation to the CS department')
    courseHistory = forms.CharField(label='Have you taken this course and if so what grade did you receive?')
    interest = forms.CharField(label='Why are you interested in being a TA for this course?')
    experience = forms.CharField(label='Please explain any relevant experience you have with course material')

    class Meta:
        model=Application
        fields = [
            'email',
            'eagleID',
            'cohort',
            'relation',
            'courseHistory',
            'interest',
            'experience',
        ]
    