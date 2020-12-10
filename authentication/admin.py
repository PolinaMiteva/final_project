from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # readonly_fields = 'id',
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email',
        'date_joined', 'is_staff', 'is_superuser', 'last_login',
    )

