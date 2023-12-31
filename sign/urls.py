from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),

    path('signup/', views.register, name="register"),
    path('activation_code_form/', views.endreg, name="endreg"),
]