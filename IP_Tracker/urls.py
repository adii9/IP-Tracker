from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('ipaddress', views.show_ip_result, name='ipaddress'),
]
