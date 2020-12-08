from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Django_fnl_project.mixins import BootstrapFormControl
from user_profile.models import Profile
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = User
        fields = "username", "password1", "password2"


class LoginForm(AuthenticationForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

