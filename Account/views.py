from django.shortcuts import render
from django.views import View

# Create your views here.
class login(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'login.html')

class registration(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'registration.html')