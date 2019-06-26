from django.contrib import admin

from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_active', 'kcal', 'protein', 'fat', 'carbo', 'fibre', 'category', 'photo_main')
    list_display_links = ('id', 'product')
    list_filter = ('category', 'is_active')
    list_editable = ('photo_main', 'is_active')
    search_fields = ('product',)
    list_per_page = 25

admin.site.register(Products, ProductsAdmin)