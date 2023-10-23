from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from common.models import User
from .models import Notification

# Create your views here.
# def Index(request):
#     users = User.objects.using('mysql_db').all()
#     user_count = users.count()
#     return render(request, 'index.html', {'user_count':user_count})

def index(request):
    users = User.objects.using('mysql_db').all()
    user_count = users.count()

    notify = Notification.objects.using('mysql_db').all()
    notify_count = notify.count()
    return render(request, 'index.html', {'user_count':user_count, 'notify_count':notify_count})

# class Index(APIView):
#     def get(self, request):
#         users = User.objects.using('mysql_db').all()
#         user_count = users.count()

#         notify = Notification.objects.using('mysql_db').all()
#         notify_count = notify.count()
#         return render(request, 'index.html', {'user_count':user_count, 'notify_count':notify_count})

# class Button(APIView):
#     def get(self, request):
#         return render(request, "buttons.html")
    
def button(request):
    return render(request, "buttons.html")
    
# class Card(APIView):
#     def get(self, request):
#         return render(request, "cards.html")
    
def card(request):
    return render(request, "cards.html")

# class Login(APIView):
#     def get(self, request):
#         return render(request, "login.html")
    
# class Register(APIView):
#     def get(self, request):
#         return render(request, "register.html")

def forgot_password(request):
    return render(request, "forgot-password.html")
    
# class Forgot_Password(APIView):
#     def get(self, request):
#         return render(request, "forgot-password.html")

def error(request):
    return render(request, "404,html")
    
# class Error(APIView):
#     def get(self, request):
#         return render(request, "404.html")

def blank(request):
    return render(request, "blank.html")

# class Blank(APIView):
#     def get(self, request):
#         return render(request, "blank.html")

def chart(request):
    return render(request, "charts.html")

# class Chart(APIView):
#     def get(self, request):
#         return render(request, "charts.html")

def notify(request):
    notify = Notification.objects.using('mysql_db').all()
    return render(request, 'notifytables.html', {'notify':notify})
    
# class Notify(APIView):
#     def get(self, request):
#         notify = Notification.objects.using('mysql_db').all()
#         return render(request, 'notifytables.html', {'notify':notify})

def delete_notification(request, index):
    if request.method == 'POST':
        # notify = get_object_or_404(Notification, pk=notify_id)
        # notify = Notification.objects.get(Index=id)      
        # notify.delete()

        notification = Notification.objects.using('mysql_db').get(Index=index)
        notification.delete()

        return redirect("main:notify")

# class Delete_notify(APIView):
#     def get(self, request, notify_id):
#         print("========")
#         print(request)
#         print("==========")
#         return redirect('/')
    
        # if request.method == 'POST':
        #     notify = get_object_or_404(Notification, pk=notify_id)
        #     notify.delete()
        #     return redirect('notify')