from django.urls import path
from apps.order import views
app_name = 'order'

urlpatterns = [
    path('', views.OrderListAPIView.as_view(), name='Order-List'),
    path('new/', views.NewOrderAPIView.as_view(), name='New-Order'),
    path('<int:pk>/', views.OrderDetailAPIView.as_view(), name='Order-Detail'),
    path('cancel/', views.CancelOrderAPIView.as_view(), name='Cancel-Order')
]
