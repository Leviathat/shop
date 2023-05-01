import os
from django.db import models
from django.utils import timezone
import random


def get_image_path(instance, filename):
    now = timezone.now()
    delta = timezone.timedelta(days=30)
    random_timestamp = now - delta * random.random()
    _, extension = os.path.splitext(filename)
    return os.path.join('products', f'{str(random_timestamp)}{extension}')


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_category'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products', db_table="product_categories")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

    @property
    def rating(self):
        reviews = self.reviews.all()
        if reviews.count() > 0:
            total_rating = sum([review.rating for review in reviews])
            return total_rating / reviews.count()
        else:
            return None


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path)

    class Meta:
        db_table = 'product_image'
