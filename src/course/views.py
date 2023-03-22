from django.shortcuts import render

from .forms import CourseCreationForm, CourseCreationFormRaw, DiscussionForm
from .models import Course, Discussion, DiscussionFormSet
from django.forms.models import modelformset_factory
# Create your views here.

def Course_Creation_View(request):
    courseForm = CourseCreationForm()
    discussionFormSet = modelformset_factory(Discussion, form=DiscussionForm, formset=DiscussionFormSet, extra=0)
    discussionForm = discussionFormSet(request.POST or None)
    context = {
        "courseForm" : courseForm,
        "discussionForm": discussionForm,
    }
    if (request.method == "POST"):
        print(request.POST)
        courseForm = CourseCreationForm(request.POST)
        discussionFormSet = modelformset_factory(Discussion, form=DiscussionForm, formset=DiscussionFormSet, extra=0)
        discussionForm = discussionFormSet(request.POST)
        if all([courseForm.is_valid(), discussionForm.is_valid()]):
            course = courseForm.save(commit=False)
            course.instructor = request.user.first_name + ' ' + request.user.last_name
            course.save()
            for form in discussionForm:
                discussion = form.save(commit=False)
                discussion.course = course
                discussion.save()
            context['message'] = 'Data saved.'
        else:
            print(courseForm.errors)
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