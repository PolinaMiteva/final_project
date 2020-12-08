from functools import wraps
from django.contrib.auth.models import User
from django.shortcuts import render

from blog.models import Comment


def required_user(view_func):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        permitted_user = User.objects.get(pk=kwargs["pk"])
        if current_user == permitted_user or current_user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, "errors/404.html")
    return wrap


def required_user_for_comment(view_func):
    def wrap(request, *args, **kwargs):
        current_user = request.user
        permitted_user = Comment.objects.get(pk=kwargs["pk"]).user
        if current_user == permitted_user or current_user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, "errors/404.html")
    return wrap