from django import forms
from .models import Course

class CourseCreationFormTest(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'courseNumber',
            'courseName',
            'courseSection',
            'courseDescription'
        ]

class CourseCreationForm(forms.Form):
    courseNumber = forms.IntegerField(label='Course Number')
    courseName = forms.CharField(label='Course Name')
    courseSection = forms.IntegerField(label='Section', widget=forms.Textarea)
    courseDescription = forms.CharField(label='Course Description')
    startTime = forms.TimeField(label='Start Time')
    endTime = forms.TimeField(label='End Time')
    hasDiscussion = forms.NullBooleanField(label='Discussion Sections')
    homeworkGradedInMeetings = forms.NullBooleanField(label='Homework graded in meetings')
    officeHoursPerWeek = forms.IntegerField(label='Office hours per week')
    relevantInfo = forms.CharField(label='Relevant info for applicants', required=False, widget=forms.Textarea)

