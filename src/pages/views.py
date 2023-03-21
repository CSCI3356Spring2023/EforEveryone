from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def logIn_view(request, *args, **kwargs):
    username = ''
    password = ''
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            group = None
            if (user.groups.exists()):
                group = user.groups.all()[0].name
            if (group == 'Admin'):
                return redirect('/adminHome')
            elif(group == 'Instructor'):
                return redirect('/instructorHome')
            elif(group == 'Student'):
                return redirect('/studentHome')
        else:
            messages.info(request, "Username or Password Incorrect")
    context = {}
    return render(request, "registration/loginPage.html", context)

def logOut_view(request):
    logout(request)
    return redirect('/logIn')

@login_required(login_url='/logIn')
def instructorHome_view(request, *args, **kwargs):
    return render(request, "instructorHome.html", {})

@login_required(login_url='/logIn')
def studentHome_view(request, *args, **kwargs):
    return render(request, "studentHome.html", {})

@login_required(login_url='/logIn')
def adminHome_view(request, *args, **kwargs):
    return render(request, "adminHome.html", {})

@login_required(login_url='/logIn')
def instructorAddCourse(request, *args, **kwargs):
    return render(request, "addCourse.html", {})

@login_required(login_url='/logIn')
def studentApplyToCourse(request, *args, **kwargs):
    return render(request, "applyToCourse.html", {})