from django.contrib import admin
from .models import Product, Category, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Category, CategoryAdmin)