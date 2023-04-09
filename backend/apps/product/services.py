from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from apps.product.models import Product


class CategoryFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    categories = CategoryFilter(field_name='categories__name', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['categories', 'price']


class ProductPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
