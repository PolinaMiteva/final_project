from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user_profile.admin import ProfileInlineAdmin


UserModel = get_user_model()
admin.site.unregister(UserModel)


class CustomUserAdmin(UserAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email',
        'date_joined', 'is_staff', 'is_superuser', 'last_login',
    )

    inlines = (
        ProfileInlineAdmin,
    )


admin.site.register(UserModel, CustomUserAdmin)
