from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView, CreateView
from authentication.forms import RegisterForm, ProfileForm


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was created successfully')
            return redirect('index')
        else:
            messages.error(request, _('Please correct the error below.'))
    elif request.method == "GET":
        user_form = RegisterForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'index.html', context={
        'user_form': user_form,
        'profile_form': profile_form
    })


