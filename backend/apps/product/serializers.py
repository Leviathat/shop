from rest_framework import serializers
from apps.product.models import Product, ProductImage, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    categories_data = serializers.CharField(write_only=True)

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000,
                                     allow_empty_file=False,
                                     use_url=False),
        write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'images', 'uploaded_images', 'categories', 'categories_data')

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        categories_data = validated_data.pop('categories_data').split()

        categories = Category.objects.filter(id__in=categories_data)
        product = Product.objects.create(**validated_data)
        product.categories.add(*categories)
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
        return product
