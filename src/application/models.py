from django.db import models
from course.models import Course
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Name')
    email = models.CharField(max_length=100, blank=True, default='Email')
    eagleID = models.IntegerField(default=0)
    courseHistory = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    applicantUser = models.ForeignKey(User, on_delete=models.CASCADE, editable = True, blank=True, null=True)

    def __str__(self):
        return str(self.course.courseNumber) + "/" + str(self.course.courseSection) + "-" + self.name