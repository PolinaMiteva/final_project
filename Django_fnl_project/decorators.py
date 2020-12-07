from functools import wraps
from django.contrib.auth.models import User
from django.shortcuts import render


def required_user(view_func):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        permitted_user = User.objects.get(pk=kwargs["pk"])
        if current_user == permitted_user:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, "errors/404.html")
    return wrap
