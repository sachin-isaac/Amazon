from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(Profile)
admin.site.register(Shipping)