from django.urls import path
from apps.product_reviews import views
app_name = 'product_reviews'

urlpatterns = [
    path('', views.MakeReviewAPIView.as_view()),
]
