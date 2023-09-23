from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.home,name="home"),
    path('login',views.login, name="login"),
    path('login2',views.login2,name="login2"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('dataanalysis.html',views.data,name="data"),
    path('courses.html',views.courses,name="courses"),
    path('trainers.html',views.train,name="train"),
    path('events.html',views.events,name='event')
]

