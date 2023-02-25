from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logIn_view(request, *args, **kwargs):
    return HttpResponse("<h1>Login page</h1>")

def instructorHome_view(request, *args, **kwargs):
    return render(request, "instructorHome.html", {})

def studentHome_view(request, *args, **kwargs):
    return render(request, "studentHome.html", {})

def adminHome_view(request, *args, **kwargs):
    return render(request, "adminHome.html", {})