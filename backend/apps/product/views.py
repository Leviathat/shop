from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters import rest_framework as filters

from apps.product.serializers import ProductSerializer
from apps.product.models import Product
from apps.product.services import ProductFilter


class ProductPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductsAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def post(self, request):
        self.check_permissions(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginator = ProductPagination()
        result_page = paginator.paginate_queryset(filtered_queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-id')
        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
