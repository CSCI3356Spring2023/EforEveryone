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
from django.urls import include, path

#Custom urls
from pages.views import adminHome_view, studentHome_view, instructorHome_view, logIn_view, logOut_view, instructorAddCourse, send_email
from course.views import Course_Creation_View
from application.views import Application_Creation_View, Application_View

urlpatterns = [
    path('', logIn_view),
    path('admin/', admin.site.urls),
    path('adminHome/', adminHome_view),
    path('instructorHome/', instructorHome_view),
    path('studentHome/', studentHome_view),
    path('add-course-form', Course_Creation_View),
    path('instructorHome/add-course', instructorAddCourse),
    #'<int:key_id>/'
    path('studentHome/apply/<int:courseID>', Application_Creation_View, name="studentApply"),
    path('instructorHome/viewApplications/<int:courseID>', Application_View, name="applicationView"),
    path('logIn/', logIn_view),
    path('logOut/', logOut_view),
    path('send_email/', send_email, name='send_email'),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
