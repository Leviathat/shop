from django.urls import path
from apps.product.views import ProductsAPIView
app_name = 'product'

urlpatterns = [
    path('', ProductsAPIView.as_view()),
]
