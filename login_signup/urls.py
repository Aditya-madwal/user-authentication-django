from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('home/',views.homeview, name = 'home'),
    # path('login/',views.loginview, name = 'login'),
    path('register/',views.registerview, name = 'register'),
    path('login/',views.loginview, name = 'login'),
    path('logout/',views.logoutview, name = 'logout'),
    path('',views.homeview, name = 'home'),
    path('tasks/',views.taskview, name = 'tasks'),
]
