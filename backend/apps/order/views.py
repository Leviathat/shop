from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.order.serializers import OrderSerializer, OrderCancellationSerializer
from apps.order.renderers import OrderJSONRenderer
from apps.order.models import Order


# class OrderAPIView(APIView):
class OrderAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    renderer_classes = (OrderJSONRenderer,)

    def post(self, request):
        order = request.data.get('order', {})
        order['customer'] = request.user.pk
        serializer = self.serializer_class(data=order)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Order.objects.filter(customer__email=self.request.user.email)


class CancelOrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderCancellationSerializer
    renderer_classes = (OrderJSONRenderer,)

    def patch(self, request):
        order_id = request.data.pop('order_id')
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OrderCancellationSerializer(instance=order, data=request.data, partial=True,
                                                 context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
