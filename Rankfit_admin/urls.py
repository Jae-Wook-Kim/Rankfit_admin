"""
URL configuration for Rankfit_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', Index.as_view(), name="index"),
    path('', include('main.urls')),

    path('common/', include('common.urls')),

    # path('notify/', Notify.as_view(), name="notify"),
    # path('delete/<int:notify_id>/', Delete_notify.as_view(), name="notify_delete"),
    # path('login/', Login.as_view(), name="login"),
    # path('signup/', Register.as_view(), name="signup"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)