from django.db import models
from apps.product.utils import get_product_image_path, get_category_image_path


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=get_category_image_path)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_category'


class ProductSize(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='product_category_sizes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_size'

    def __str__(self):
        return f'{self.name} --- {self.category}'


class Product(models.Model):
    in_stock = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name='products', db_table="product_categories")
    sizes = models.ManyToManyField(ProductSize, related_name='products', db_table="product_sizes")

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
    image = models.ImageField(upload_to=get_product_image_path)

    class Meta:
        db_table = 'product_image'

