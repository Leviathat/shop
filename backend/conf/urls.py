from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.authentication.urls')),
    path('api/products/', include('apps.product.urls')),
    path('api/order/', include('apps.order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
