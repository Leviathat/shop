from django.urls import path
from apps.order.views import OrderAPIView, CancelOrderAPIView
app_name = 'order'

urlpatterns = [
    path('', OrderAPIView.as_view()),
    path('cancel/', CancelOrderAPIView.as_view()),
]
