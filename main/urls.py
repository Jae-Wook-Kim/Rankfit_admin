from django.urls import path
from . import views
from django.conf.urls.static import static
from Rankfit_admin import settings

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),

    path('notify/', views.notify, name="notify"),
    path('notify/delete/<int:index>/', views.delete_notification, name="delete_notification"),

    path('notice/', views.notice, name="notice"),
    path('notice/delete/<int:index>/', views.delete_notice, name="delete_notice"),
    path('notice/new', views.new_notice, name="new_notice"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)