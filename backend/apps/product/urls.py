from django.urls import path
from . views import ProductsAPIView
app_name = 'product'

urlpatterns = [
    path('', ProductsAPIView.as_view())
]
