from django.db import models
from django.contrib.auth.models import User
import uuid
from djmoney.models.fields import MoneyField

class Category(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    image=models.ImageField(null=True,blank=True)
    description=models.TextField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class meta:
        db_table="category"    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False,blank=False)
    vender=models.CharField(max_length=20,null=False,blank=False)
    product_image=models.ImageField(null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name        

    class meta:
        db_table="product"    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table="cart"

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price 

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  

    class Meta:
        db_table="favourite"
    
class Payment(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    amount=models.IntegerField(null=False)
    #currency=MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    payment_mode=models.CharField(max_length=20,null=False)
    payment_status=(('Pending','Pending'),('In Progress','In Progress'),('Completed','Completed'),('Failed','Failed'))
    status=models.CharField(max_length=50,choices=payment_status,default="Completed")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.amount,self.status)

class Shipping(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    fname=models.CharField(max_length=20, null=False)
    lname=models.CharField(max_length=20, null=False)
    phone=models.BigIntegerField(null=False)
    address=models.TextField(null=False)
    landmark=models.CharField(max_length=40)
    country=models.CharField(max_length=20, null=False)
    state=models.CharField(max_length=20, null=False)
    city=models.CharField(max_length=20, null=False)
    pincode=models.IntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  

    def __str__(self):
        return '{} - {}'.format(self.fname,self.city)    
    
class Orderz(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    shipping=models.ForeignKey(Shipping,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    quantity=models.IntegerField(null=False)
    price=models.IntegerField(null=False)
    order_status=(('Pending','Pending'),('Out For Shipping','Out For Shipping'),('Completed','Completed'),('Cancelled','Cancel'))
    status=models.CharField(max_length=50,choices=order_status,default="Pending")
    tracking_no=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return '{} - {}'.format(self.user,self.product.name)  
     
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images',null=True,blank=True,default="uploads\pf.jpg")
    fname=models.CharField(max_length=20, null=True)
    lname=models.CharField(max_length=20, null=True)
    dob=models.DateField(null=True)
    email=models.EmailField(null=True)
    phone=models.BigIntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.username
    
class Myaddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    address_head = models.CharField(max_length=20)
    fname=models.CharField(max_length=20, null=False)
    lname=models.CharField(max_length=20, null=False)
    phone=models.BigIntegerField(null=False)
    address=models.TextField(null=False)
    landmark=models.CharField(max_length=40)
    country=models.CharField(max_length=20, null=False)
    state=models.CharField(max_length=20, null=False)
    city=models.CharField(max_length=20, null=False)
    pincode=models.IntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  

    def __str__(self):
        return '{} - {}'.format(self.fname,self.address_head)
    
class Orderscancelled(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    order=models.ForeignKey(Orderz,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    reason =models.CharField(max_length=50, null=False)
    describe=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.user,self.order.product,self.reason)