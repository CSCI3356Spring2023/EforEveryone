from django import forms
from .models import Course, Discussion
from django.forms.models import inlineformset_factory

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

class CourseCreationForm(forms.ModelForm):
    courseNumber = forms.IntegerField(label='Course Number')
    courseName = forms.CharField(label='Course Name')
    courseSection = forms.IntegerField(label='Section')
    courseDescription = forms.CharField(label='Course Description', widget=forms.Textarea)
    days = forms.MultipleChoiceField(choices=DAYS_OF_WEEK, widget=forms.CheckboxSelectMultiple)
    startTime = forms.TimeField(label='Start Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    endTime = forms.TimeField(label='End Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    hasDiscussion = forms.NullBooleanField(label='Discussion Sections')
    homeworkGradedInMeetings = forms.NullBooleanField(label='Homework graded in meetings')
    officeHoursPerWeek = forms.IntegerField(label='Office hours per week')
    relevantInfo = forms.CharField(label='Relevant info for applicants', required=False, widget=forms.Textarea)
    
    class Meta:
        model = Course
        fields = [
            'courseNumber',
            'courseName',
            'courseSection',
            'courseDescription',
            'days',
            'startTime',
            'endTime',
            'hasDiscussion',
            'homeworkGradedInMeetings',
            'officeHoursPerWeek',
            'relevantInfo'
        ]
             


class CourseCreationFormRaw(forms.Form):
    courseNumber = forms.IntegerField(label='Course Number')
    courseName = forms.CharField(label='Course Name')
    courseSection = forms.IntegerField(label='Section')
    courseDescription = forms.CharField(label='Course Description', widget=forms.Textarea)
    startTime = forms.TimeField(label='Start Time', widget=forms.TimeInput)
    endTime = forms.TimeField(label='End Time',widget=forms.TimeInput)
    hasDiscussion = forms.NullBooleanField(label='Discussion Sections')
    homeworkGradedInMeetings = forms.NullBooleanField(label='Homework graded in meetings')
    officeHoursPerWeek = forms.IntegerField(label='Office hours per week')
    relevantInfo = forms.CharField(label='Relevant info for applicants', required=False, widget=forms.Textarea)

class DiscussionForm(forms.ModelForm):
    startTime = forms.TimeField(label='Start Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    endTime = forms.TimeField(label='End Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    days = forms.MultipleChoiceField(choices=DAYS_OF_WEEK)
    class Meta:
        model = Discussion
        fields = (
            'discussionNumber',
            'days',
            'startTime',
            'endTime'
        )
