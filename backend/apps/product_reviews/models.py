from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from apps.authentication.models import User
from apps.product.models import Product


class ProductReview(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='reviews')
    comment = models.TextField(blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'product')
        db_table = 'product_reviews'

    def __str__(self):
        return f"{self.customer.email} - {self.product.name} - {self.rating}"
