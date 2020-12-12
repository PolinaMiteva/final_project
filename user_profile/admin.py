from django.contrib import admin
from user_profile.models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


admin.site.register(Profile)