from rest_framework import serializers
from apps.product.models import Product
from apps.order.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'created_at', 'updated_at', 'products', 'total_amount')

    def get_products(self, order):
        order_products = OrderProduct.objects.filter(order=order).select_related('product')
        return OrderProductSerializer(order_products, many=True).data

    def get_status_display(self, obj):
        return dict(Order.STATUS_CHOICES)[obj.status]


class NewOrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, write_only=True)
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'status', 'status_display', 'created_at', 'products', 'total_amount', 'customer', )
        read_only_fields = ('id', 'created_at', 'status_display', 'status', )

    def validate_products(self, products):
        if not products:
            raise serializers.ValidationError('Must be at least one product to make order')
        return products

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            OrderProduct.objects.create(
                order=order,
                product=Product.objects.get(id=product_data['product'].pk),
                quantity=product_data['quantity']
            )

        return order

    def get_status_display(self, obj):
        return dict(Order.STATUS_CHOICES)[obj.status]


class OrderCancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']
        read_only_fields = ('status', )

    def validate(self, attrs):
        order = self.instance
        request = self.context.get('request')

        if request.user.id != order.customer_id:
            raise serializers.ValidationError('You are not authorized to cancel this order')
        elif order.status == 5:
            raise serializers.ValidationError('Order is already cancelled')
        return attrs

    def update(self, instance, validated_data):
        instance.status = 5
        instance.save()
        return instance

