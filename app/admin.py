from django.contrib import admin
from .models import Home, Product, Category
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name', 'details')
    list_filter = ('category',)
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)