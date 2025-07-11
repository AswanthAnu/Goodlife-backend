from django.contrib import admin
from .models import CustomUser, Customer, CustomerAddress, Product, ProductVariant, ProductPricing, Order, OrderDetails, Delivery, Cart, CartItem, Category, CustomerLocation, DealOfTheDay, OfferCartItem

# Register your models here.
class ProductPricingInline(admin.TabularInline):
    model = ProductPricing
    extra = 1

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    inlines = [ProductPricingInline]
    extra = 1

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductPricingInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline ]
    search_fields = ['category__category_name', 'product_name']

class CartItemVariantInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemVariantInline]

class CustomerLocationInline(admin.TabularInline):
    model = CustomerLocation
    extra = 0

class CustomerAddressInline(admin.TabularInline):
    inlines = [CustomerLocationInline]
    model = CustomerAddress
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerAddressInline]
    search_fields = [ 'first_name', 'last_name', 'phone_number']

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailsInline]
    search_fields = ['customer__first_name']

class DeliveryAdmin(admin.ModelAdmin):
    search_fields = ['order__customer__first_name', 'order__customer__last_name']

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'username']




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress)
admin.site.register(CustomerLocation)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductPricing)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(DealOfTheDay)
admin.site.register(OfferCartItem)
