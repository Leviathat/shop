from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters import rest_framework as filters

from apps.product.renderers import ProductJSONRenderer, CategoryJSONRenderer
from apps.product.serializers import ProductSerializer, CategoryListSerializer
from apps.product.models import Product, Category
from apps.product.services import ProductFilter, ProductPagination


class ProductRetrieveAPiView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ProductSerializer
    renderer_classes = (ProductJSONRenderer,)
    queryset = Product.objects.all()


class ProductsAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    renderer_classes = (ProductJSONRenderer,)

    def post(self, request):
        self.check_permissions(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset).distinct()
        paginator = ProductPagination()
        result_page = paginator.paginate_queryset(filtered_queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def get_queryset(self):
        q = Product.objects.all().order_by('-id')
        return q

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class CategoriesAPIView(generics.GenericAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (AllowAny, )
    renderer_classes = (CategoryJSONRenderer,)

    def post(self, request):
        self.check_permissions(request)
        category = request.data.get('category', {})
        serializer = self.serializer_class(data=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        q = Category.objects.all().order_by('-id')
        return q

    
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]