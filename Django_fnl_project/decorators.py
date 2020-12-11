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


def required_group_user(view_func):
    def wrap(request, *args, **kwargs):
        groups = ['writers']
        user = request.user
        if not user.is_authenticated:
            return render(request, "errors/404.html")

        groups_set = set(groups or [])
        raw_groups = request.user.groups.all()
        user_groups = set([group.name for group in raw_groups])

        if not user_groups.intersection(groups_set) and not user.is_superuser:
            return render(request, "errors/404.html")
        else:
            return view_func(request, *args, **kwargs)

    return wrap