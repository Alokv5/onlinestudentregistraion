from django.shortcuts import render,redirect
from app1.models import adminModel,New_shedule,Student,CourseModel
from django.views.generic import ListView,TemplateView,CreateView,DeleteView,UpdateView,RedirectView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
def index(request):
     return render(request, "admin.html")

def validate(request):
     usr=request.POST.get("e1")
     psd=request.POST.get("p1")
     try:
          res= adminModel.objects.get(email=usr,password=psd)
          return render(request,"login_details.html",{"data":res})
     except adminModel.DoesNotExist:
          return render(request, "admin.html", {"error_msg": "invalid input"})

def shedule_new(request):
     return render(request,"new_class.html")

def register_class(request):
     name=request.POST.get("t1")
     faculty=request.POST.get("t2")
     date=request.POST.get("t3")
     time=request.POST.get("t4")
     fee=request.POST.get("t5")
     duration=request.POST.get("t6")
     New_shedule(name=name,faculty=faculty,date=date,time=time,fee=fee,duration=duration).save()
     messages.success(request,"Class Shedule Save Successfully")
     return redirect("shedule_new")


def view_all_class(request):
     result=New_shedule.objects.all()
     return render(request,"view_class.html",{"data":result})

# def allcourse(request):
#      res=New_shedule.objects.all()
#      return render(request,"view_class.html",{"data":res})
def update_class(request):
    id=request.GET.get("t1")
    res=New_shedule.objects.get(idno=id)
    return render(request ,"update_class.html",{"data":res})

def save_update(request):
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    fa=request.POST.get("t3")
    date=request.POST.get("t4")
    time=request.POST.get("t5")
    fee=request.POST.get("t6")
    dur=request.POST.get("t7")
    New_shedule.objects.filter(idno=idno).update(name=name,faculty=fa,date=date,time=time,fee=fee,duration=dur)
    return redirect("view_all_class")

def delete_class(request):
    no=request.GET.get("no")
    New_shedule.objects.filter(idno=no).delete()
    return redirect("view_all_class")


def student_index(request):
     return render(request,"student_index.html")

def student_registration(request):
     return render(request,"student_registration.html")

def save_registration(request):
     idno=request.POST.get("s1")
     name=request.POST.get("s2")
     contact=request.POST.get("s3")
     email=request.POST.get("s4")
     passw=request.POST.get("s5")
     Student(idno=idno,name=name,contact=contact,email=email,password=passw).save()
     messages.success(request," Registerd successfully")
     return redirect("student_index")

def student_login(request):
     return render(request,"student_login.html")

def login_validation(request):
     usr=request.POST.get("l1")
     pasd=request.POST.get("l2")
     try:
           res=Student.objects.get(email=usr,password=pasd)
           return render (request, "welcome_page.html", {"data":res})
     except Student.DoesNotExist:
          return render(request,"student_login.html",{"error":"Invalid Input"})


class  welcome_page(TemplateView):
     template_name =  "welcome_page.html"

class enrol_course(SuccessMessageMixin,CreateView):
     template_name = "enrol_course.html"
     model = CourseModel
     fields = "__all__"
     success_url = '/welcome_page/'
     success_message = " Student Enrolled Successfully"

class view_all_enroll(ListView):
     template_name = "view_all Enroll.html"
     model = CourseModel
     #queryset = CourseModel.objects.values("idno","name")

class cancel_class(DeleteView):
     template_name = "cancel.html"
     model = CourseModel
     success_url = '/welcome_page/'

class OpenFacbook(RedirectView):
    url = "https://www.facebook.com/"