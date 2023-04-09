from django.urls import path
from apps.product import views
app_name = 'product'

urlpatterns = [
    path('', views.ProductsAPIView.as_view()),
    path('<int:pk>/', views.ProductRetrieveAPiView.as_view()),
    path('categories/', views.CategoriesAPIView.as_view())
]
