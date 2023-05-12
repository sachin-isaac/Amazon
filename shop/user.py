from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    try:
        products=Product.objects.filter(trending=1)
        return render(request,"products/home.html",{"products":products})
    except Exception as e:
        print(e)


def login_page(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method=='POST':
                usr=request.POST.get('username')
                pwd=request.POST.get('password')
                user=authenticate(request,password=pwd,username=usr)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return redirect("home")
                else:
                    messages.error(request,'Invalid Username or Password')
                    return redirect('login')    
            return render(request,'user/login.html')
    except Exception as e:
        print(e) 
        return redirect('home')


def logout_page(request):
    try:
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,'Logout Successfully')
        return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')


def register(request): 
    try:
        form=UserForm()
        if request.method=='POST':
            form=UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registration Success You can Login Now ...!")
                return redirect('login')
        return render(request,"user/register.html",{"form":form})    
    except Exception as e:
        print(e)
        return redirect('home')        