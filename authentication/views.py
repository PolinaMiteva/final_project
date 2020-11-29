from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from authentication.forms import RegistrationForm, ProfileForm


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


def profile_details(request):
    pass


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
            return redirect('index')
    elif request.method == 'GET':
        user_form = RegistrationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)

    return render(request, 'update_profile.html',
                  context={'user_form': user_form, 'profile_form': profile_form})


class CustomLogIn(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = 'index.html'
    success_message = 'Welcome to your profile'






