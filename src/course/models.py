from django.db import models
from django.forms.models import BaseModelFormSet

# Create your models here.
class Course(models.Model):
    courseNumber = models.IntegerField(default=0)
    courseName = models.CharField(max_length=100, blank=True, default='Name')
    courseSection = models.IntegerField(default=0)
    courseDescription = models.TextField(blank=True, null=True, default='Description')
    instructor = models.CharField(default='Instructor', max_length=100)
    days = models.CharField(default='', max_length=100)
    startTime = models.TimeField(default='00:00:00')
    endTime = models.TimeField(default='00:00:00')
    hasDiscussion = models.BooleanField(default=False, null=False)
    homeworkGradedInMeetings = models.BooleanField(default=False, null=False)
    officeHoursPerWeek = models.IntegerField(default=0)
    relevantInfo = models.TextField(blank=True, null=True)
    numberOfTAs = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

class Discussion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    discussionNumber = models.IntegerField(default=0)
    days = models.CharField(default='', max_length=100)
    startTime = models.TimeField(default='00:00:00')
    endTime = models.TimeField(default='00:00:00')

class DiscussionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(DiscussionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Discussion.objects.none()