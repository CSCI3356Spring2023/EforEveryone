from django.db import models
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver 

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
    instructorUser = models.ForeignKey(User, on_delete=models.CASCADE, editable = False, blank=True, null=True)

    def __str__(self):
        return str(self.courseNumber) + "/" + str(self.courseSection) + " " + self.courseName

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

# Extending the User model using a one-to-one link
# Add the field to keep track of the number of open applications (max 5)

# Define signals so our Profile model will be automatically 
# created/updated when we create/update User instances.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usedApplications = models.PositiveIntegerField(default=0, blank=False, null=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()