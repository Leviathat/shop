from typing import Iterable, Optional
from django.db import models
from apps.product.models import Product
from apps.authentication.models import User
from django.dispatch import receiver


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        (1, 'Оформлен'),
        (2, 'Оплачен'),
        (3, 'В пути'),
        (4, 'Доставлен'),
        (5, 'Отменен'),
        (6, 'Товар не в наличии'),
    ]
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='OrderProduct')
    
    @property
    def total_amount(self):
        order_products = OrderProduct.objects.filter(order=self)
        total = sum(op.product.price * op.quantity for op in order_products)
        return total
    
    def __str__(self):
        return f'Order #{self.pk}'

    class Meta:
        db_table = 'order'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    class Meta:
        db_table = 'order_product'

@receiver(models.signals.post_save, sender=OrderProduct)
def update_order_status(sender, instance, **kwargs):
    order = instance.order
    if order.products.filter(in_stock=False).exists():
        order.status = 6
        order.save(update_fields=['status'])