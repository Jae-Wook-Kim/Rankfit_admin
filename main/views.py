from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class Index(APIView):
    def get(self, request):
        return render(request, "index.html")

class Button(APIView):
    def get(self, request):
        return render(request, "buttons.html")
    
class Card(APIView):
    def get(self, request):
        return render(request, "cards.html")

class Login(APIView):
    def get(self, request):
        return render(request, "login.html")
    
class Register(APIView):
    def get(self, request):
        return render(request, "register.html")
    
class Forgot_Password(APIView):
    def get(self, request):
        return render(request, "forgot-password.html")
    
class Error(APIView):
    def get(self, request):
        return render(request, "404.html")

class Blank(APIView):
    def get(self, request):
        return render(request, "blank.html")