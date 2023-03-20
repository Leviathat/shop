from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.authentication.urls')),
    path('products/', include('apps.product.urls')),
]
