import os

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from Django_fnl_project.decorators import required_user
from user_profile.forms import UpdateProfile, UpdateUser
from user_profile.models import Profile


@login_required
def details(request, pk=None):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
        'can_edit': True if request.user == user or request.user.is_superuser else False,
    }

    return render(request, 'details.html', context=context)


@required_user
@login_required
def update_profile(request, pk):
    if request.method == "GET":
        user_form = UpdateUser(instance=User.objects.get(pk=pk))
        profile_form = UpdateProfile(instance=Profile.objects.get(user_id=pk))
        context = {
            'profile': profile_form,
            'user': user_form,
        }
        return render(request, 'update_profile.html', context)
    elif request.method == "POST":
        current_user = User.objects.get(pk=pk)
        current_profile = Profile.objects.get(user_id=pk)
        current_picture = current_user.profile.picture.name[17:]

        user_form = UpdateUser(request.POST, instance=current_user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=current_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()

            # if request.FILES.get('picture'):
            #     pic_name = request.FILES.get('picture').name
            #     if pic_name != current_picture and current_picture != '':
            #         os.remove(current_user.profile.picture.path)
            return redirect('details', pk=request.user.pk)

        context = {
            'user': user_form,
            'profile': profile_form,
        }

        return render(request, 'update_profile.html', context)
