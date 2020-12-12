# from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render


class BootstrapFormControl:
    def setup_form(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_control()

    def form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class GroupRequiredMixin:
    groups = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return render(request, "errors/404.html")

        groups_set = set(self.groups or [])
        raw_groups = user.groups.all()
        user_groups = set([group.name for group in raw_groups])

        if not user_groups.intersection(groups_set) and \
                not user.is_superuser:
            return render(request, "errors/404.html")

        return super().dispatch(request, *args, **kwargs)


class LogoutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)

