from django.shortcuts import render, redirect

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
            course.instructorUser = request.user
            course.save()
            for form in discussionForm:
                discussion = form.save(commit=False)
                discussion.course = course
                discussion.save()
            context['message'] = 'Data saved.'
            return redirect('instructorHome')
        else:
            print(courseForm.errors)
    return render(request, "addCourseForm.html", context)

def Course_Edit_View(request, courseID):
    course = Course.objects.get(id = courseID)
    courseForm = CourseCreationForm(instance = course)
    context = {
        "courseForm" : courseForm,
        "course" : course
    }
    if (request.method == "POST"):
        courseForm = CourseCreationForm(request.POST, instance = course)
        if all([courseForm.is_valid()]):
            course = courseForm.save()
            context['message'] = 'Data saved.'
            return redirect('instructorHome')
        else:
            print(courseForm.errors)
    return render(request, "editCourseForm.html", context)

def Course_Edit_View_Admin(request, courseID):
    course = Course.objects.get(id = courseID)
    courseForm = CourseCreationForm(instance = course)
    context = {
        "courseForm" : courseForm,
        "course" : course
    }
    if (request.method == "POST"):
        courseForm = CourseCreationForm(request.POST, instance = course)
        discussionFormSet = modelformset_factory(Discussion, form=DiscussionForm, formset=DiscussionFormSet, extra=0)
        discussionForm = discussionFormSet(request.POST or None)
        if all([courseForm.is_valid(), discussionForm.is_valid()]):
            course = courseForm.save()
            context['message'] = 'Data saved.'
            return redirect('adminHome')
        else:
            print(courseForm.errors)
    return render(request, "adminEditCourseForm.html", context)
    
def Course_Delete_View(request, courseID):
    course = Course.objects.get(id = courseID)
    courseForm = CourseCreationForm(instance = course)
    context = {
        "courseForm" : courseForm,
    }

    if request.method == 'POST':       
        course.delete()          
        return redirect('instructorHome') 

    return render(request, "editCourseForm.html", context)    

def Course_Delete_View_Admin(request, courseID):
    course = Course.objects.get(id = courseID)
    courseForm = CourseCreationForm(instance = course)
    context = {
        "courseForm" : courseForm,
    }

    if request.method == 'POST':       
        course.delete()          
        return redirect('/adminHome') 

    return render(request, "adminEditCourseForm.html", context)  
            


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