from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainshop.urls')),
    path('account/', include('Account.urls')),
    path('cart/', include('Cart.urls')),
]
