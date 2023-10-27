from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        print("Success!!")
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username= request.POST['email'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, '../templates/register.html')
    return render(request, '../templates/register.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
        else:
            form = AuthenticationForm()
        context = {
            'form' : form,
        }
        return render(request, '../templates/login.html', context)
    
# @require_POST
def logout(request):
    auth_logout(request)
    return redirect('/')

def user_list(request):
    users=User.objects.using('mysql_db').all()
    return render(request, '../templates/usertables.html', {'users':users})