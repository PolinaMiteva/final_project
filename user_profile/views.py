import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from Django_fnl_project.decorators import required_user
from user_profile.forms import UpdateProfile, UpdateUser
from user_profile.models import Profile


# class Details(LoginRequiredMixin, TemplateView):
#     template_name = 'details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = User.objects.get(pk=args['pk'])
#         return context


@login_required
def details(request, pk=None):
    # user = request.user if pk is None else User.objects.get(pk=pk)
    user = User.objects.get(pk=pk)
    return render(request, 'details.html', context={'user': user})


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
        current_picture = Profile.objects.get(user_id=request.user.pk).picture
        user_form = UpdateUser(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user = user_form.save()
            if request.FILES:
                if request.FILES['picture'] != current_picture:
                    user.profile.picture = request.FILES['picture']
                    if current_picture != 'default_user.png':
                        os.remove(current_picture.path)
            user.save()
            profile_form.save()
            return redirect('details', pk=request.user.pk)

        context = {
            'user': user_form,
            'profile': profile_form,
        }

        return render(request, 'update_profile.html', context)
