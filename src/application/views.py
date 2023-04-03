from django.shortcuts import render
from .forms import ApplicationCreationForm
from course.models import Course
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
            application = applicationForm.save(commit=False)
            application.course = course
            application.name = request.user.first_name + ' ' + request.user.last_name
            application.applicantUser = request.user
            application.save()
            context['message'] = 'Data saved.'
        else:
            print(applicationForm.errors)
    return render(request, "applyToCourse.html", context)


