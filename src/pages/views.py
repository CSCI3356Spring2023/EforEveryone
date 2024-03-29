from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from course.models import Profile
from django.contrib.auth.models import User

from course.models import Course
from application.models import Application

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
def profile_view(request, username): 
    user = get_object_or_404(User, username=request.user.username)

    context = {
        "user" : user,
    }
    return render(request, 'profilePage.html', context)

@login_required(login_url='/logIn')
def instructorHome_view(request, *args, **kwargs):
    courseDataAll = Course.objects.all().order_by('-created_at')
    courseDataUser = Course.objects.filter(instructorUser=request.user).order_by('-created_at')
    applications = Application.objects.all().order_by('-created_at')
    instructor_applications = []
    for application in applications:
        if application.course in courseDataUser:
            instructor_applications.append(application)

    context = {
        "all_courses" : courseDataAll,
        "user_courses" : courseDataUser,
        "all_applications" : instructor_applications
    }
    return render(request, "instructorHome.html", context)

@login_required(login_url='/logIn')
def cant_hire_page(request):
    return render(request,"cant_hire.html")


@login_required(login_url='/logIn')
def studentHome_view(request, *args, **kwargs):
    courseDataAll = Course.objects.all().order_by('-created_at')
    applications = Application.objects.filter(applicantUser = request.user).order_by('-created_at')
    appliedCourses=[]
    for application in applications:
        appliedCourses.append(application.course)

    closedCourses = 0
    courses = Course.objects.all()
    courseCount = Course.objects.all().count()

    for c in courses:
        if (c.numberOfAcceptedTAs == c.numberOfTAs):
            closedCourses += 1
    if (closedCourses == courseCount):
        return redirect('/system-closed')
    else:
        context = {
            "all_courses" : courseDataAll,
        "applied_courses" : appliedCourses,
            "applications" : applications
        }
        return render(request, "studentHome.html", context)


# def system_closed(request):
#     return redirect("systemClosed.html")
@login_required(login_url='/logIn')
def systemClosed(request, *args, **kwargs):
    return render(request, "systemClosed.html", {})


@login_required(login_url='/logIn')
def adminHome_view(request, *args, **kwargs):
    courseDataAll = Course.objects.all()
    context = {
        "all_courses" : courseDataAll
    }
    return render(request, "adminHome.html", context)

@login_required(login_url='/logIn')
def instructorAddCourse(request, *args, **kwargs):
    return render(request, "addCourse.html", {})

@login_required(login_url='/logIn')
def studentApplyToCourse(request, *args, **kwargs):
    return render(request, "applyToCourse.html", {})

def send_email(request):
    subject = 'Test Email'
    message = 'Hello this is a test'
    sender_email = 'sender@example.com'
    recipient_list = [request.user.email]
    
    send_mail(
        subject=subject,
        message=message,
        from_email=sender_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    
    return render(request, 'email_sent.html')

