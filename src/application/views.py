from django.shortcuts import render, get_object_or_404
from .forms import ApplicationCreationForm
from course.models import Course, Profile
from application.models import Application
# Create your views here.


def Application_Creation_View(request, courseID):
    applicationForm = ApplicationCreationForm()
    course = Course.objects.get(id = courseID)

    context = {
        "applicationForm" : applicationForm,
        "course" : course,
    }
    if (request.method == "POST"):
        applicationForm = ApplicationCreationForm(request.POST)
        if (applicationForm.is_valid()):
            profile = get_object_or_404(Profile, user=request.user)
            
            # if profile.usedApplications > 5 {
            #     print("You have 5 applications in review and cannot submit anymore at this time.") 
            # }

            # otherwise do everything correctly
            
            profile.usedApplications += 1
            profile.save()
            application = applicationForm.save(commit=False)
            application.course = course
            application.name = request.user.first_name + ' ' + request.user.last_name
            application.applicantUser = request.user
            application.save()
            context['message'] = 'Data saved.'
        else:
            print(applicationForm.errors)
    return render(request, "applyToCourse.html", context)


def Application_View(request, courseID):
    course = Course.objects.get(id = courseID)
    applications = Application.objects.filter(course = course)
    context = {
        "course" : course,
        "course_applications" : applications
    }
    return render(request, "applicationView.html", context)
