from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

from .models import Course, Discussion
# Register your models here.
class DiscussionInline(admin.StackedInline):
    model = Discussion
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [DiscussionInline]
    list_display = ['__str__', 'spots_filled', 'status']

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class CustomizedUserAdmin (UserAdmin):
    inlines = (ProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Course, CourseAdmin)
