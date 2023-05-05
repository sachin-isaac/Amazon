from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.http import JsonResponse
import json
from django.core.paginator import *

def fav(request):    
    try:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data=json.load(request)
                product_id=data['pid']
                product_status=Product.objects.get(id=product_id)
                if product_status:
                    if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({'status':'Product already in Favourite'}, status=200)
                    else:
                        Favourite.objects.create(user=request.user,product_id=product_id)
                        return JsonResponse({'status':'Product added to Favourite'},status=200)
            else:
                return JsonResponse({'status':'Login to Add Favourite'},status=200)

        else:
            return JsonResponse({'status':'Invalid Access'}, status=200)
    except Exception as e:
        print(e) 
        return redirect('home')   

def fav_page(request):
    try:
        if request.user.is_authenticated:
            fav=Favourite.objects.filter(user=request.user)
            return render(request,'cart/fav.html',{"fav":fav})
        else:
            return redirect("home")
    except Exception as e:
        print(e)    
        return redirect('home')

def remove_fav(request,fid):
    try:
        fitem=Favourite.objects.get(id=fid)
        fitem.delete()
        return redirect('fav_page')    
    except Exception as e:
        print(e)
        return redirect('home')