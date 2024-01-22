from django import forms
from .models import register
from django.forms.widgets import TextInput, PasswordInput

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register_form(forms.ModelForm):
    class Meta:
        model = register
        fields = "__all__"
        widgets = {
            "username":  TextInput(attrs={'placeholder':'ex:test','autocomplete': 'off'}), 
            "password": PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
        }
        labels = {
            "username": None,
            "password": None
        }

class user_registeration_form(UserCreationForm) :
    # now this user_registeration_form is just a replica of the real usercreationform since we called it as arg in the brackets
    class Meta :
        model = User
        # now this is why we imported user model from auth
        fields = ['username', 'email', 'password1', 'password2']