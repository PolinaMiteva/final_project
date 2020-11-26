from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import Profile


class ProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Profile
        fields = "__all__"


class LogInForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = "__all__"


