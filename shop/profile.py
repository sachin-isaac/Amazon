from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages

def profile(request):
    try:
        pf=Profile.objects.filter(user=request.user)
        user = request.user
        psform = SetPasswordForm(user)
        if pf:
            profile=request.user.profile
            form=ProfileForm(instance=profile)
            for i in pf:
                day=i.dob.day
                month=i.dob.month
            if day==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                day=str(0)+str(day)
            if month==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                month=str(0)+str(month)   
            return render(request,"user/profile.html",{"pf":pf,"day":day,"month":month,"form":form,"psform":psform}) 
        else:
            form=ProfileForm()
            return render(request,"user/profile.html",{"psform":psform,"form":form})
    except Exception as e:
        print(e) 
        return redirect('home')    
    
def new_profile(request):
    try:    
        if request.method =="POST":
            Profile.objects.create(
                user=request.user,
                fname=request.POST.get('fname'),
                lname=request.POST.get('lname'),
                email=request.POST.get('email'),
                dob=request.POST.get('dob'),
                phone=request.POST.get('phone')
            )    
            profile=request.user.profile
            form=ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
            messages.success(request,"Profile Updated")
        else:
                messages.info(request,"Profile Not Updated")    
        return redirect('profile')    

    except Exception as e:
        print(e) 
        return redirect('home')    
    
def update_profile(request):
    try:    
        if request.method == "POST":
            i=Profile.objects.get(user=request.user)
            i.fname=request.POST.get('fname')
            i.lname=request.POST.get('lname')
            i.email=request.POST.get('email')
            i.phone=request.POST.get('phone')
            i.dob=request.POST.get('dob')
            i.save()

            profile=request.user.profile
            form=ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Updated")
            else:
                messages.info(request,"Profile Not Updated")
   
        return redirect('profile')    

    except Exception as e:
        print(e) 
        return redirect('home') 
    
def update_password(request):
    try:
        if request.method == 'POST':
            user=request.user
            psform = SetPasswordForm(user, request.POST)
            if psform.is_valid():
                psform.save()
                messages.success(request, "Your password has been changed")
                return redirect('home')
            else:
                for error in list(psform.errors.values()):
                    messages.error(request, error) 
        return redirect('profile')    
    except Exception as e:
        print(e) 
        return redirect('home')
    
      