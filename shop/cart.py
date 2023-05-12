from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.http import JsonResponse
import json
from django.core.paginator import *

def addto_cart(request):    
    try:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_qty=data['product_qty']
                product_id=data['pid']
                product_status=Product.objects.get(id=product_id)
                if product_status:
                    if Cart.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'Product already in cart'}, status=200)
                    else:
                        if product_status.quantity>=product_qty:
                            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                            return JsonResponse({'status':'Product added to the cart'},status=200)
                        else:
                            return JsonResponse({'status':'Product Stock Not available'},status=200)
                        
                return JsonResponse({"status":"Product Added to cart"},status=200)
            else:
                return JsonResponse({'status':'Login to Add Cart'},status=200)

        else:
            return JsonResponse({'status':'Invalid Access'}, status=200)
    except Exception as e:
        print(e) 
        return redirect('home')   
    

def cart_page(request):
    try:
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            total_price=0
            for item in cart:
                total_price += item.total_cost
            return render(request,'cart/cart.html',{"cart":cart,"total_price":total_price})
        else:
            return redirect("home")
    except Exception as e:
        print(e)   
        return redirect('home') 
    
    
def remove_cart(request,cid):
    try:
        citem=Cart.objects.get(id=cid)
        citem.delete()
        return redirect('cart')
    except Exception as e:
        print(e)
        return redirect('home')