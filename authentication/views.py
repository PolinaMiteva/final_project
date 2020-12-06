from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.forms import RegistrationForm, LoginForm
from user_profile.forms import ProfileForm
from django.contrib.auth.views import LoginView


# @transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            messages.success(request, 'Your profile was created successfully!')
            return redirect('index')
        else:
            user_form = RegistrationForm(request.POST)
            messages.warning(request, 'Correct the errors bellow.')
            return render(request, template_name='register.html', context={'user_form': user_form})
    elif request.method == 'GET':
        user_form = RegistrationForm()

    return render(request, template_name='register.html', context={'user_form': user_form})


class LogInView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@transaction.atomic
def profile_update(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect('index')
    elif request.method == 'GET':
        user_form = RegistrationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)

    return render(request, 'update_profile.html',
                  context={'user_form': user_form, 'profile_form': profile_form})


# def get_redirect_url(params):
#     redirect_url = params.get('return_url')
#     return redirect_url if redirect_url else 'index'







