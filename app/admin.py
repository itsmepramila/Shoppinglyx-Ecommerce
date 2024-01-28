from django.contrib import admin
from app.models import Customer, Product, Cart, OrderPlaced

# Register your models here.
# admin.site.register(Customer)
# admin.site.register(Product)

# admin.site.register(Cart)
# admin.site.register(OrderPlaced)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name', 'city', 'zipcode', 'state']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title','selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'product', 'quantity']
    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']