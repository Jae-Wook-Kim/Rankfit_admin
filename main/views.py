from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from common.models import User
from .models import Notification, Notice

def index(request):
    users = User.objects.using('mysql_db').all()
    user_count = users.count()

    notify = Notification.objects.using('mysql_db').all()
    notify_count = notify.count()
    return render(request, 'index.html', {'user_count':user_count, 'notify_count':notify_count})

def notify(request):
    notify = Notification.objects.using('mysql_db').all()
    return render(request, 'notifytables.html', {'notify':notify})

def delete_notification(request, index):
    if request.method == 'POST':
        notification = Notification.objects.using('mysql_db').get(Index=index)
        notification.delete()
        return redirect("main:notify")

def notice(request):
    notice = Notice.objects.using('mysql_db').all()
    return render(request, 'noticetables.html', {'notice':notice})

def delete_notice(request, index):
    if request.method == 'POST':
        notice = Notice.objects.using('mysql_db').get(index=index)
        notice.delete()
        return redirect("main:notice")

    
def button(request):
    return render(request, "buttons.html")
    
def card(request):
    return render(request, "cards.html")

def forgot_password(request):
    return render(request, "forgot-password.html")

def error(request):
    return render(request, "404,html")

def blank(request):
    return render(request, "blank.html")

def chart(request):
    return render(request, "charts.html")