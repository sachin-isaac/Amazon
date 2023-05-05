from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages

def my_orders(request):
    try:
        orders=Orders.objects.filter(user=request.user)
        return render(request,'order/orders.html',{"orders":orders})
    except Exception as e:
        print(e)   
        return redirect('home') 
    
def order_details(request,oid):
    try:
        order= Orders.objects.filter(id=oid).filter(user=request.user).first()
        if order:
            return render(request,'order/orderdetails.html',{"order":order})
        else:
            return redirect('my_orders')
    except Exception as e:
        print(e)   
        return redirect('home') 
    
def cancel_order(request):
    try:
        oid=request.POST.get("order_id")
        order= Orders.objects.filter(id=oid).filter(user=request.user).first()
        order.status="Cancelled"
        order.save()
        orderproduct = Product.objects.filter(id=order.product_id).first()
        orderproduct.quantity=orderproduct.quantity+order.quantity
        orderproduct.save()
        messages.success(request,"Your Order is Cancelled")
        return redirect('my_orders')
    except Exception as e:
        print(e)   
        return redirect('home')