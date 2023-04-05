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
