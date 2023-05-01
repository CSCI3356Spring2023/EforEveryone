from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ApplicationCreationForm
from django.contrib.auth.models import User
from course.models import Course, Profile
from application.models import Application
from django.core.mail import send_mail
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
            
            print(profile.usedApplications)
            if profile.usedApplications >= 5:
                print("You have 5 applications in review and cannot submit anymore at this time.") 
            else:
                print("You can submit this application")
                profile.usedApplications += 1
                profile.save()
                application = applicationForm.save(commit=False)
                application.course = course
                application.name = request.user.first_name + ' ' + request.user.last_name
                application.applicantUser = request.user
                application.save()
                # context['message'] = 'Data saved.'
            # otherwise do everything correctly
            
            # profile.usedApplications += 1
            # profile.save()
            # application = applicationForm.save(commit=False)
            # application.course = course
            # application.name = request.user.first_name + ' ' + request.user.last_name
            # application.applicantUser = request.user
            # application.save()
            context['message'] = 'Data saved.'
            print(profile.usedApplications)
        else:
            print(applicationForm.errors)
        return redirect('studentHome')
    return render(request, "applyToCourse.html", context)


def Application_View(request, courseID):
    course = Course.objects.get(id = courseID)
    applications = Application.objects.filter(course = course).order_by('-created_at')
    context = {
        "course" : course,
        "course_applications" : applications
    }
    return render(request, "applicationView.html", context)

def Admin_Application_View(request, courseID):
    course = Course.objects.get(id = courseID)
    applications = Application.objects.filter(course = course).order_by('-created_at')
    openTAPositions = course.numberOfTAs - course.numberOfAcceptedTAs
    context = {
        "course" : course,
        "openTAPositions": openTAPositions,
        "course_applications" : applications
    }
    return render(request, "adminApplicationView.html", context)

def accept_application(request, application_id):
    # Get the application object from the database
    application = get_object_or_404(Application, id=application_id)
    course = Course.objects.get(courseName = application.course.courseName)

    # Send an email to the student associated with the application
    send_mail(
        'Your application has been accepted',
        'Congratulations! Your application for {} has been accepted.'.format(application.course),
        'from@example.com',
        [application.email],
        fail_silently=False,
    )

    # Mark the application as accepted by instructor in the database
    application.pendingInstructorAccept = False
    application.save()

    # Redirect to the application list page
    return redirect('instructorHome')

def reject_application(request, application_id):
    # Get the application object from the database
    application = get_object_or_404(Application, id=application_id)

    # Send an email to the student associated with the application
    send_mail(
        'You application was not accepted',
        'Unfortunately, your application for {} has not been accepted.'.format(application.course),
        'from@example.com',
        [application.email],
        fail_silently=False,
    )

    # Remove the applications
    application.delete()

    # Redirect to the application list page
    return redirect('instructorHome')

def student_accept_application(request, application_id):
    # Get the application object from the database
    application = get_object_or_404(Application, id=application_id)
    course = Course.objects.get(courseName = application.course.courseName)
    profile = get_object_or_404(Profile, user=request.user)

    # Send an email to the student associated with the application
    send_mail(
        'You have accepted to be a TA',
        'Congratulations! Your application for {} has been accepted.'.format(application.course),
        'from@example.com',
        [application.email],
        fail_silently=False,
    )

    # Mark the application as accepted in the database, update the course status if needed
    course.numberOfAcceptedTAs += 1
    if course.numberOfAcceptedTAs == course.numberOfTAs:
        course.status = False
    course.save()

    application.acceptedByStudent = True
    application.save()

    profile.usedApplications = 5
    profile.save()

    for application in Application.objects.filter(applicantUser = request.user):
        if application.id != application_id:
            application.delete()
            
    # Redirect to the application list page
    return redirect('studentHome')

