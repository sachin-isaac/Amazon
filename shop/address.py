from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages
from django.utils import timezone

def address(request):
    try:
        Address=Myaddress.objects.filter(user=request.user)
        print(timezone.now())
        return render(request,'address/address.html',{"address":Address})
    except Exception as e:
        print(e) 
        return redirect('home')  


def new_address(request):
    try:
        return render(request,'address/newaddress.html')
    except Exception as e:
        print(e) 
        return redirect('home')
    

def add_address(request):
    try:
        if request.method=="POST":
            Myaddress.objects.create(
                user=request.user,
                address_head = request.POST.get("address_head"),
                fname= request.POST.get("fname"),
                lname=request.POST.get("lname"),
                phone=request.POST.get("phone"),
                address=request.POST.get("address"),
                landmark=request.POST.get("landmark"),
                country=request.POST.get("country"),
                state=request.POST.get("state"),
                city=request.POST.get("city"),
                pincode=request.POST.get("pincode"),
            )
            messages.success(request,"New Address added successfully")
            return redirect('address')    
    except Exception as e:
        print(e) 
        messages.info(request,"Error while adding new address")
        return redirect('home')
    

def edit_address(request,aid):
    try:
        addrezz=Myaddress.objects.get(id=aid)
        return render(request,'address/updateaddress.html',{"a":addrezz})
    except Exception as e:
        print(e) 
        return redirect('home')    
    

def update_address(request):
    try:
        if request.method=="POST":
            aid=request.POST.get("aid")
            a= Myaddress.objects.filter(id=aid).filter(user=request.user).first()
            a.address_head=request.POST.get("address_head")
            a.fname=request.POST.get("fname")
            a.lname=request.POST.get("lname")
            a.phone=request.POST.get("phone")
            a.address=request.POST.get("address")
            a.landmark=request.POST.get("landmark")
            a.country=request.POST.get("country")
            a.state=request.POST.get("state")
            a.city=request.POST.get("city")
            a.pincode=request.POST.get("pincode")
            a.save()
            messages.info(request,"Address updated successfully")
            return redirect("address")
        else:
            messages.info(request,"Address is not updated")
            return redirect("address")
    except Exception as e:
        print(e) 
        return redirect('address')    
    

def delete_address(request,aid):
    try:
        addrezz=Myaddress.objects.get(id=aid)
        addrezz.delete()
        messages.success(request,"Address deleted successfully")
        return redirect('address')
    except Exception as e:
        print(e) 
        return redirect('address')    