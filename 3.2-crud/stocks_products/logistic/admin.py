from django.contrib import admin
from .models import Stock, Product, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    list_display = ['quantity', 'price']
    extra = 0

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    inlines = [StockProductInline, ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
