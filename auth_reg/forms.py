from django.db import models
from django.contrib.auth.models import User
from .models import *
from django import forms
from django import views
from .models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)