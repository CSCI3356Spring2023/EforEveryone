from django.shortcuts import render

from .forms import CourseCreationForm, CourseCreationFormRaw
from .models import Course
# Create your views here.

def Course_Creation_View(request):
    form = CourseCreationForm()
    if (request.method == "POST"):
        form = CourseCreationForm(request.POST)
        if (form.is_valid()):
            print(form.cleaned_data)
            Course.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form" : form
    }
    return render(request, "addCourseForm.html", context)

# def Course_Creation_View(request):
#     print(request.method)
#     form = CourseCreationFormTest(request.POST or None)
#     if (form.is_valid()):
#         form.save()
#         form = CourseCreationFormTest()
#     context = {
#         'form': form
#     }
#     return render(request, "addCourseForm.html", context)