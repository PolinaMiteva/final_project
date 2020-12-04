from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from user_profile.forms import UpdateProfile, UpdateUser
from user_profile.models import Profile


@login_required()
def details(request, pk):
    return render(request, 'details.html', context={'user': User.objects.get(pk=request.user.pk)})


@login_required()
def update_profile(request, pk):
    if request.method == "GET":
        user_form = UpdateUser(instance=request.user)
        profile_form = UpdateProfile(instance=request.user.profile)
        context = {
            'profile': profile_form,
            'user': user_form,
        }
        return render(request, 'update_profile.html', context)
    elif request.method == "POST":
        current_picture = Profile.objects.get(user_id=request.user.pk).picture
        user_form = UpdateUser(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user = user_form.save()
            if request.FILES:
                if request.FILES['picture'] != current_picture:
                    user.profile.picture = request.FILES['picture']
            user.save()
            profile_form.save()
            return redirect('index')

        context = {
            'user': user_form,
            'profile': profile_form,
        }

        return render(request, 'update_profile.html', context)

