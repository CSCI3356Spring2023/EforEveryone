from django.db import models
from course.models import Course
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='Name')
    email = models.CharField(max_length=100, blank=True, default='Email')
    eagleID = models.IntegerField(default=0)
    courseHistory = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    applicantUser = models.ForeignKey(User, on_delete=models.CASCADE, editable = True, blank=True, null=True)
    pendingInstructorAccept = models.BooleanField(default=True)
    acceptedByStudent = models.BooleanField(default=False)
    rejectedByStudent = models.BooleanField(default=False)
    COHORT_CHOICES = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    ]
    cohort = models.CharField(max_length=20, choices=COHORT_CHOICES, blank=True, null=True)
    RELATION_CHOICES = [
        ('Major BS', 'Major BS'),
        ('Major BA', 'Major BA'),
        ('Minor', 'Minor'),
        ('Other', 'Other'),
    ]
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.course.courseNumber) + "/" + str(self.course.courseSection) + "-" + self.name