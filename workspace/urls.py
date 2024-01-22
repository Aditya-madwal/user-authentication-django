from django.contrib import admin
from django.urls import path, include
from login_signup import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_signup.urls')),
]
