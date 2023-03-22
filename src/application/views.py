from django.shortcuts import render
from .forms import ApplicationCreationForm


# Create your views here.


def Application_Creation_View(request):
    applicationForm = ApplicationCreationForm()
    context = {
        "applicationForm" : applicationForm,
    }
    if (request.method == "POST"):
        print(request.POST)
        applicationForm = ApplicationCreationForm(request.POST)
        if (applicationForm.is_valid()):
            application = applicationForm.save(commit=False)
            application.name = request.user.first_name + ' ' + request.user.last_name
            application.save()
            context['message'] = 'Data saved.'
        else:
            print(applicationForm.errors)
    return render(request, "applyToCourse.html", context)


