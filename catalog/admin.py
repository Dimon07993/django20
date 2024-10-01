from django.contrib import admin
from .models import Category, Product, Version

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created_at', 'updated_at', 'description',)
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')



@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')


