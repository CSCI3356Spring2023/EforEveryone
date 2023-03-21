from django.contrib import admin

from .models import Course, Discussion
# Register your models here.
class DiscussionInline(admin.StackedInline):
    model = Discussion
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [DiscussionInline]

admin.site.register(Course, CourseAdmin)