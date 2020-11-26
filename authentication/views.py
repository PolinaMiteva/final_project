from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, DeleteView
from authentication.forms import ProfileForm
from django.utils.decorators import method_decorator
# from authtools.views import LoginView, LogoutView


class RegisterProfileView(CreateView):
    template_name = 'user_profile.html'
    #change to next url
    success_url = '/'
    form_class = ProfileForm
    success_message = "Your profile was created successfully"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
        # see how to send email
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    template_name = 'user_profile.html'
    # change to next url
    success_url = '/'
    form_class = ProfileForm
    success_message = "Your profile was successfully deleted!"


