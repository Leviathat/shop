from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductImageSerializer
from .models import Product
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductsAPIView(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = Product.objects.all().order_by('-id')
        paginator = ProductPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)



