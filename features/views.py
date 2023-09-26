from django.shortcuts import render
from django.http import HttpResponse
from .models import user_info,school_dropout_data,Scheme_Table





# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if(request.method == "GET"):
        return render(request,"login.html")
    if(request.method == "POST"):
        return login_helper(request)


def login_helper(request):
    if(request.POST.get("userName") == ""):
        return render(request,"login.html")
    
    elif(request.POST.get("passWord") == ""):
        return render(request,"login.html")
    
    userName = request.POST["userName"]
    passWord = request.POST["passWord"]

    if( not user_info.objects.filter( user_name = userName , password = passWord ).exists() ):
        return render(request,"login.html",{"error" : True})
    
    return render(request,"index.html",{"login":True})

def pieChart(request):
    SchoolId = request.POST["school-id"]
    PrincipalId = request.POST["principal_id"]
    EducationNum = request.POST["no_of_students_ed"]
    EconomicNum = request.POST["no_of_students_eco"]
    MedicalNum = request.POST["no_of_students_med"]

    temp = Scheme_Table(schoolId =SchoolId, principalId = PrincipalId, education_num = EducationNum, economic_num = EconomicNum, medical_num = MedicalNum)
    temp.save()


    content = {
        'school':SchoolId,
        'education':EducationNum,
        'economic':EconomicNum,
        'medical':MedicalNum
    }

    return render(request,"Pie_chart.html",content)

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def course_detail(request):
    return render(request,"course-details.html")

def courses(request):
    return render(request,"courses.html")
    
def train(request):
    return render(request,"trainers.html")

def events(request):
    return render(request,"events.html")

def contact(request):
    return render(request,"contact.html")

def scheme(request):
    return render(request,"Scheme.html")


def data(request):
    school_names = []
    district_names = []
    drop_out_number = []
    dict = {}
    objects = school_dropout_data.objects.all()

    for objs in objects:
        school_names.append(objs.school_name)
        district_names.append(objs.school_district)
        drop_out_number.append(objs.drop_out_number)
        dict[objs.school_name] = objs.school_district 
    
    districtNames = list(set(district_names))
    
    context = {
        'school_names' : school_names,
        'district_names' : districtNames,
        'drop_out_number' : drop_out_number,
        'dict':dict
    }

    
    return render(request, 'dataanalysis.html', context)

def dropout(request):
    return render(request,"dropout_analysis.html")

def stud_reg(request):
    return render(request,"student_registration.html")



