from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.home,name="home"),
    path('login.html',views.login_user, name="login"),
    path('logout',views.logout_user,name="logout"),
    path('course-details.html',views.course_detail,name="course_details"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('dataanalysis.html',views.data,name="dataanalysis"),
    path('courses.html',views.courses,name="courses"),
    path('trainers.html',views.train,name="train"),
    path('events.html',views.events,name='event'),
    path('dropout_analysis.html',views.dropout,name="dropout_analysis"),
    path('student_registration.html',views.stud_reg,name="student_registration"),
    path('Scheme.html',views.scheme,name="scheme"),
    path('Pie.html',views.pieChart,name="Pie")
]

