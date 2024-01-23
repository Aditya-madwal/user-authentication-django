from django import forms
from .models import *
from django.forms.widgets import TextInput, PasswordInput

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class user_registeration_form(UserCreationForm) :
    # now this user_registeration_form is just a replica of the real usercreationform since we called it as arg in the brackets
    class Meta :
        model = User
        # now this is why we imported user model from auth
        fields = ['username', 'email', 'password1', 'password2']

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','desc']
