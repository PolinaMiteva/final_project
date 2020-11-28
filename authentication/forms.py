from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import Profile


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            # field.widget.attrs.update({'class': 'form-group'})


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = "picture",
