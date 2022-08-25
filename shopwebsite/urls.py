from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainshop.urls')),
    path('account/', include('Account.urls')),
    path('cart/', include('Cart.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
