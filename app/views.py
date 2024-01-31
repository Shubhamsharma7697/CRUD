from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    stu=Student.objects.all()
    return render(request,'app/home.html',{'stu':stu})

def add_stu(request):
    if request.method=="POST":
        # print("added")
        #retrive the user input
        stu_roll=request.POST.get("stu_roll")
        stu_name=request.POST.get("stu_name")
        stu_email=request.POST.get("stu_email")
        stu_address=request.POST.get("stu_address")
        stu_phone=request.POST.get("stu_phone")

        #create sn object for model class
        s=Student()
        s.roll=stu_roll
        s.name=stu_name
        s.email=stu_email
        s.address=stu_address
        s.phone=stu_phone

        s.save()



        return redirect("/home/")
    return render(request,'app/add_stu.html',{})



def delete_stu(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/home/")

def update_stu(request,roll):
    stu=Student.objects.get(pk=roll)
    return render(request,'app/update_stu.html',{'stu':stu})

def do_update_stu(request,roll):
    stu_roll=request.POST.get("stu_roll")
    stu_name=request.POST.get("stu_name")
    stu_email=request.POST.get("stu_email")
    stu_address=request.POST.get("stu_address")
    stu_phone=request.POST.get("stu_phone")
    s=Student.objects.get(pk=roll)
    s.roll=stu_roll
    s.name=stu_name
    s.email=stu_email
    s.address=stu_address
    s.phone=stu_phone
    s.save()
    return redirect("/home/")

