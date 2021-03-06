from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class StandardUserForm(ModelForm):
    class Meta:
        model = StandardUser
        fields = "__all__"

class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

class StandardUserForm(ModelForm):
    class Meta:
        model = StandardUser
        fields = "__all__"
