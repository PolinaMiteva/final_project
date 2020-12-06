from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = 'picture', 'phone_number'


class UpdateUser(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()
        # self.fields['username'].widget.attrs.update(disabled=True)

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email',


class UpdateProfile(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = 'picture', 'phone_number'