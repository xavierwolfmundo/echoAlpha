from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'in_stock')
    list_filter = ('in_stock',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'is_completed')
    list_filter = ('order_date', 'is_completed')
    search_fields = ('user__username', 'user__email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
