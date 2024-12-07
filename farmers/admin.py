from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models.farmers import Farmer
from .models.customer import Customer
from .models.products import Product
from .models.orders import Order

# Customize Farmer Admin
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'password','phone','image')
    

# Customize Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'password','phone','image')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('email',)

# Customize Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category','image','farmer')
    search_fields = ('name', 'category')
    list_filter = ('category',)

# Customize Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','customer','quantity','price','address','date','status')
    search_fields = ('customer', 'product')



