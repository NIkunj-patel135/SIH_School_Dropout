from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.home,name="home"),
    path('login',views.login, name="login"),
    path('course-details.html',views.course_detail,name="course_detail"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('dataanalysis.html',views.data,name="data"),
    path('courses.html',views.courses,name="courses"),
    path('trainers.html',views.train,name="train"),
    path('events.html',views.events,name='event'),
    path('dropout_analysis.html',views.dropout,name="dropout"),
    path('student_registration.html',views.stud_reg,name="student_registration")
]

