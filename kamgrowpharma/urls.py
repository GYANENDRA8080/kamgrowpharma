from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('orders/', include('apps.orders.urls')),
    path('prescriptions/', include('apps.prescriptions.urls')),
    path('cart/', include('apps.cart.urls')),
    path('api/catalog/', include('apps.catalog.api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
