from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_profile.models import Profile
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = "username", "password1", "password2"


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    # class Meta:
    #     model = User
    #     fields = 'user', 'password'
