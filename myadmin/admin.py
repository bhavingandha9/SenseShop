from django.contrib import admin
from .models import payments,temp_cart,product,order_details,stock,complaint
from login.models import customer

# Register your models here.

admin.site.register(payments)

admin.site.register(temp_cart)
admin.site.register(product)
admin.site.register(order_details)
admin.site.register(stock)
admin.site.register(complaint) 
# admin.site.register(retail_stock)
# admin.site.register(warehouse_stock) 