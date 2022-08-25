from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainshop.urls')),
    path('account/', include('Account.urls')),
    path('cart/', include('Cart.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
