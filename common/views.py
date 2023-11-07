from django.contrib import auth, messages
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import User

# Create your views here.

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        else:
            try:
                user = User.objects.create_user(email=email, password=password1)
                user = authenticate(request, email=email, password=password1)
                auth_login(request, user)
                return redirect('/')
            except ValidationError as e:
                messages.error(request, e.message)
    return render(request, '../templates/register.html')
    
def login(request):
    if request.method == 'POST':
        print(request)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, '이메일 혹은 비밀번호가 올바르지 않습니다.')
    return render(request, '../templates/login.html')
    
# @require_POST
def logout(request):
    auth_logout(request)
    return redirect('/')

def user_list(request):
    users=User.objects.using('mysql_db').all()
    return render(request, '../templates/usertables.html', {'users':users})