from django.db import models

# Create your models here.
class Course(models.Model):
    courseNumber = models.IntegerField(default=0)
    courseName = models.CharField(max_length=100, blank=True, default='Name')
    courseSection = models.IntegerField(default=0)
    courseDescription = models.TextField(blank=True, null=True, default='Description')
    instructor = models.CharField(default='Instructor', max_length=100)
    #dayOfTheWeek = customFields.DayOfTheWeekField()
    startTime = models.TimeField(default='00:00:00')
    endTime = models.TimeField(default='00:00:00')
    hasDiscussion = models.BooleanField(default=False, null=False)
    homeworkGradedInMeetings = models.BooleanField(default=False, null=False)
    officeHoursPerWeek = models.IntegerField(default=0)
    relevantInfo = models.TextField(blank=True, null=True)