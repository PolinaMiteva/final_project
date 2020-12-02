from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from authentication.forms import RegistrationForm
from user_profile.forms import ProfileForm


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
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


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


# Login and LogOut - customize more
# def login_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': LoginForm(),
#         }
#
#         return render(request, 'login.html', context)
#     else:
#         login_form = LoginForm(request.POST)
#         return_url = request.POST.get('return_url', 'index')
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect(return_url)
#
#         context = {
#             'form': login_form,
#         }
#
#         return render(request, 'login.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')




