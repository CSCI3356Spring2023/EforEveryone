from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
# Create your views here.
def logIn_view(request, *args, **kwargs):
    return HttpResponse("Hello")
#return render(request, "registration/login.html", {})

def instructorHome_view(request, *args, **kwargs):
    return render(request, "instructorHome.html", {})

def studentHome_view(request, *args, **kwargs):
    return render(request, "studentHome.html", {})

def adminHome_view(request, *args, **kwargs):
    return render(request, "adminHome.html", {})

def instructorAddCourse(request, *args, **kwargs):
    return render(request, "addCourse.html", {})

def studentApplyToCourse(request, *args, **kwargs):
    return render(request, "applyToCourse.html", {})