from django.contrib import admin
from .models import Product, Customer,Category,Cart

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','category', 'image')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    list_editable = ('price', 'stock')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('date_joined',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'quantity', 'added_at')
    search_fields = ('user__username', 'products__name')
    list_filter = ('added_at',)
