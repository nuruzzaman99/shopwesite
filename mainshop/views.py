from django.shortcuts import render
from django.views import View

# Create your views here.
class index(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'index.html')

class shop(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'shop.html')

class shopDetail(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'shopDetail.html')

class contact(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'contact.html')

class shoppingCart(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'shoppingCart.html')

class checkout(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'checkout.html')