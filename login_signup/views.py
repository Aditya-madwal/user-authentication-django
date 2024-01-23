from django.shortcuts import render, redirect
from .models import *
from.forms import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerview(request) :
    if request.user.is_authenticated :
        return redirect(homeview)
    else :
        form = user_registeration_form(request.POST)

        context = {
            'form' :form,
        }

        if request.method == 'POST' :
            if form.is_valid() :
                form.save()
                username = request.POST['username']
                messages.success(request, f"jjeyy baat, {username}")
                return redirect(loginview)

        return render(request, 'register.html', context=context)

def loginview(request) :
    if request.user.is_authenticated :
        return redirect(homeview)

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        # this user is a user object and authenticate function is checking if username and password are valid as credentials or not ... if not then user = none

        if user is not None :
            # login into the website
            login(request, user)
            return redirect(homeview)
        else :
            # authentication failed
            messages.error(request, "username or password is incorrect")
            pass
    return render(request, 'login.html', {})

def logoutview(request) : 
    logout(request)
    return redirect(loginview)

@login_required(login_url=loginview)
def homeview(request) : 
    return render(request, 'home.html', {})

@login_required(login_url=loginview)
def taskview(request) :
    form = taskform(request.POST)
    tasks_list = task.objects.filter(author = request.user)

    context = {
        'form' : form,
        'tasks' : tasks_list,
    }

    if request.method == "POST" :
        if form.is_valid() :
            title = request.POST['title']
            desc = request.POST['desc']
            new_task = task(title = title, desc = desc, author = request.user)
            new_task.save()
            return redirect(taskview)
        else :
            messages.error(request, "invalid input")

    return render(request, 'tasks.html', context = context)
