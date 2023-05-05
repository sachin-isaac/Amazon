from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import *

def product_list(request):
    try:
        products = Product.objects.filter(status=0).values_list("name",flat=True)    
        productslist = list(products)
        return JsonResponse(productslist,safe=False)
    except Exception as e:
        print(e)

def search_product(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains =searchedterm).first()

            if product:
                return redirect('collections/'+product.category.name+'/'+product.name)
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get('HTTP_REFERER')) 
    else:
        return redirect(request.META.get('HTTP_REFERER'))        

def collections(request):
    try:
        category=Category.objects.filter(status=0)
        return render(request,"products/collections.html",{"category":category}) 
    except Exception as e:
        print(e) 
        return redirect('home')
    
def view(request,name):
    try:
        if(Category.objects.filter(name=name,status=0)):
            productz=Product.objects.filter(category__name=name)
            paginator = Paginator(productz, 4)
            page = request.GET.get('page')

            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
            except:
                return redirect(request.META.get('HTTP_REFERER'))    

            return render(request,"products/products.html",{"page":page,"products":products,"category_name":name})  
        else:
            messages.warning(request,"No such category Found")
            return redirect('collections')
    except Exception as e:
        print(e)   
        return redirect('home') 

def details(request,cname,pname):
    try:
        if(Category.objects.filter(name=cname,status=0)):
            if(Product.objects.filter(name=pname,status=0)): 
                products=Product.objects.filter(name=pname,status=0).first()
                return render(request,'products/details.html',{"products":products,})
            else:
                messages.error(request,'No Such Product Found')
                return redirect('collections')
        else:
            messages.error(request,'No Such Category Found')
            return redirect("collections")    
    except Exception as e:
        print(e) 
        return redirect('home')