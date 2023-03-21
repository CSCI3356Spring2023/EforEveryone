"""webProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Custom urls
from pages.views import adminHome_view, studentHome_view, instructorHome_view, logIn_view, instructorAddCourse, studentApplyToCourse
from course.views import Course_Creation_View

urlpatterns = [
    path('', logIn_view, name="LogIn"),
    path('admin/', admin.site.urls),
    path('adminHome/', adminHome_view),
    path('instructorHome/', instructorHome_view),
    path('studentHome/', studentHome_view),
    path('add-course-form', Course_Creation_View),
    path('instructorHome/add-course', instructorAddCourse),
    path('studentHome/apply', studentApplyToCourse),
]
