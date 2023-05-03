from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
