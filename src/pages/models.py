from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'admin'
        STUDENT = "STUDENT",'student'
        INSTRUCTOR = "INSTRUCTOR", 'instructor'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)
        
class Student(User):
    base_role = User.Role.STUDENT

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"

class InstructorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.INSTRUCTOR)
        
class Instructor(User):
    base_role = User.Role.INSTRUCTOR

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for instructors"
    

        