from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from authentication.models import Profile


class Details(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'details.html'
    context_object_name = 'user'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # user = context['user']
    #     context['profile'] = Profile.objects.filter(user_id=self.request.user.id)

        # return context


class UpdateProfile(DetailView):
    pass
