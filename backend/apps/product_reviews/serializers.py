from rest_framework import serializers
from apps.product_reviews.models import ProductReview


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = ('id', 'product', 'customer', 'comment', 'rating', 'created_at', )
        read_only_fields = ('id', 'created_at', )
