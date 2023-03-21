from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Name')
    email = models.CharField(max_length=100, blank=True, default='Email')
    eagleID = models.IntegerField(default=0)
    courseHistory = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)