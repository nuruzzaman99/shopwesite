"""shopwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('shop', views.shop.as_view(), name='shop'),
    path('shopDetail', views.shopDetail.as_view(), name='shopDetail'),
    path('contact', views.contact.as_view(), name='contact'),
    path('shoppingCart', views.shoppingCart.as_view(), name='shoppingCart'),
    path('checkout', views.checkout.as_view(), name='checkout'),
]
