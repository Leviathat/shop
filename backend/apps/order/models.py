from django.db import models
from apps.product.models import Product
from apps.authentication.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        (1, 'Draft'),
        (2, 'Paid'),
        (3, 'Shipped'),
        (4, 'Delivered'),
        (5, 'Cancelled'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Order #{self.pk}'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
