from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'common'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    # path('login/', LoginView.as_view(template_name="../templates/login.html"), name='login'),
    path('logout/', logout, name='logout'),
    path('users/', user_list, name='users'),
]