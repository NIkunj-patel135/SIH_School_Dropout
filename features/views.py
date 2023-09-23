from django.shortcuts import render
from django.http import HttpResponse
from .models import user_info

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login2.html")


def login2(request):
    if(request.POST.get("userName") == ""):
        return render(request,"login2.html")
    
    elif(request.POST.get("passWord") == ""):
        return render(request,"login2.html")
    
    userName = request.POST["userName"]
    passWord = request.POST["passWord"]

    if( not user_info.objects.filter( user_name = userName , password = passWord ).exists() ):
        return render(request,"login2.html",{"error" : True})
    
    return render(request,"index.html")

def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def courses(request):
    return render(request,"courses.html")
def train(request):
    return render(request,"trainers.html")
def events(request):
    return render(request,"events.html")
def contact(request):
    return render(request,"contact.html")
def data(request):
    return render(request,"dataanalysis.html")