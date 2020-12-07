from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from Django_fnl_project.mixins import BootstrapFormControl
from .models import Profile


class ProfileForm(forms.ModelForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Profile
        fields = 'picture', 'phone_number'


class UpdateUser(UserChangeForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email',


class UpdateProfile(UserChangeForm, BootstrapFormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


    class Meta:
        model = Profile
        fields = 'picture', 'phone_number'