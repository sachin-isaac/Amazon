from django.shortcuts import render,redirect
from .models import *
from shop.forms import *
from django.contrib import messages
from django.http import JsonResponse
import uuid
from django.core.paginator import *

def checkout(request):
    try:
        rawcart=Cart.objects.filter(user=request.user)
        for item in rawcart:
            if item.product_qty > item.product.quantity:
                Cart.Objects.delete(id=item.id)
                return JsonResponse({'status':'Product Stock Not available'},status=200)
        cartitems=Cart.objects.filter(user=request.user)
        total_price=0
        for item in cartitems:
            total_price += item.total_cost

        pf = Shipping.objects.filter(user=request.user).first()
    
        return render(request,'cart/checkout.html',{"cartitems":cartitems,"total_price":total_price,"pf":pf})
    except Exception as e:
        print(e)
        return redirect('home')

def remove_checkout(request,cid):
    try:
        citem=Cart.objects.get(id=cid)
        citem.delete()
        return redirect('checkout')
    except Exception as e:
        print(e) 
        return redirect('home')       

def placeorder(request):
    try:
        if request.method == 'POST': 
            payment=Payment()
            payment.amount=request.POST.get('total_amount')
            payment.payment_mode=request.POST.get('payment_mode')
            payment.save()

            shipping=Shipping()
            shipping.user = request.user
            shipping.fname = request.POST.get('fname')
            shipping.lname = request.POST.get('lname')
            shipping.email = request.POST.get('email')
            shipping.phone = request.POST.get('phone')
            shipping.address = request.POST.get('address')
            shipping.landmark=request.POST.get('landmark')
            shipping.country = request.POST.get('country')
            shipping.state = request.POST.get('state')
            shipping.city = request.POST.get('city')
            shipping.pincode = request.POST.get('pincode')
            shipping.save()
            
            neworderitems = Cart.objects.filter(user=request.user)
            for item in neworderitems:
                Orders.objects.create(
                    user=request.user,
                    product=item.product,
                    payment=payment,
                    shipping=shipping,
                    quantity=item.product_qty,
                    price=item.product.selling_price,
                    tracking_no=uuid.uuid4()
                )

                orderproduct = Product.objects.filter(id=item.product_id).first()
                orderproduct.quantity=orderproduct.quantity-item.product_qty
                orderproduct.save()
  

            Cart.objects.filter(user=request.user).delete()   

            messages.success(request,"Your Order has been placed sucessfully")     
        return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')
    
def buy(request,cname,pname):
    try:
        if request.user.is_authenticated:    
            qty= request.POST.get('qty')
            if(Category.objects.filter(name=cname,status=0)):
                    if(Product.objects.filter(name=pname,status=0)): 
                        products=Product.objects.filter(name=pname,status=0).first()
                        if products.quantity>=int(qty):
                            pf = Shipping.objects.filter(user=request.user).first()
                            total=int(products.selling_price)*int(qty)
                            return render(request,'cart/buy.html',{"products":products,"qty":qty,"total":total,"pf":pf})
                        else:
                            return JsonResponse({'status':'Product Stock Not available'},status=200) 
        else:
            return JsonResponse({'status':'Login to Buy Now'},status=200)            
    except Exception as e:
        print(e)
        return redirect('home')
        
def buy_placeorder(request):
    try:
        if request.method == 'POST':
            payment=Payment()
            payment.amount=request.POST.get('total_amount')
            payment.payment_mode=request.POST.get('payment_mode')
            payment.save()

            shipping=Shipping()
            shipping.user = request.user
            shipping.fname = request.POST.get('fname')
            shipping.lname = request.POST.get('lname')
            shipping.email = request.POST.get('email')
            shipping.phone = request.POST.get('phone')
            shipping.address = request.POST.get('address')
            shipping.landmark=request.POST.get('landmark')
            shipping.country = request.POST.get('country')
            shipping.state = request.POST.get('state')
            shipping.city = request.POST.get('city')
            shipping.pincode = request.POST.get('pincode')
            shipping.save()

            pid=request.POST.get('pid')
            qty=request.POST.get('qty')
            price=request.POST.get('price')

            product_status=Product.objects.get(id=pid)
            if product_status:
                if product_status.quantity>=int(qty):
                    Orders.objects.create(
                                user=request.user,
                                product_id=pid,
                                payment=payment,
                                shipping=shipping,
                                quantity=int(qty),
                                price=int(price),
                                tracking_no=uuid.uuid4()
                            )
                    
                    orderproduct = Product.objects.filter(id=pid).first()
                    orderproduct.quantity=orderproduct.quantity-int(qty)
                    orderproduct.save()
                    messages.success(request,"Your Order has been placed sucessfully") 
                else:
                    return JsonResponse({'status':'Product Stock Not available'},status=200)   
        return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')