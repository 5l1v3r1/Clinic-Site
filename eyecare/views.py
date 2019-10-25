from django.shortcuts import render , redirect
from .models import appointment , regis
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phnumber')
        subject=request.POST.get('subject')
        message = request.POST.get('message')

        user = appointment(name=name,phone=phone,subject=subject,message=message)
        user.save()
        mess = "Your appointment have been sent successfully"
        return render(request,"index.html",{'mess':mess})
    else:
        return render(request,"index.html")


def login1(request):

    if request.method=="POST":
        username = request.POST.get('username1','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)

            return redirect("main")
        else:

            return redirect('login1')
    else:
        return render(request,"login1.html")

@login_required(login_url='http://127.0.0.1:8000/login1')
def main(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        username = request.POST.get('username','')
        phone = request.POST.get('email','')
        location = request.POST.get('password','')
        day  = request.POST.get('birthday_date','')
        month = request.POST.get('month','')
        year = request.POST.get('year','')
        gender = request.POST.get('gender','')
        user = regis(first_name=name,last_name=username,phone=phone,location=location,day=day,month=month,year=year,gender=gender)
        user.save()
        return redirect('main')
    return render(request,"main.html")


def search(request):
    search_query = request.POST.get('search_query')
    myposts = regis.objects.filter(phone=search_query , first_name=search_query)
    mycount = regis.objects.all().count()
    return render(request,"search.html",{'mycount' :mycount , 'myposts' : myposts })
