from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'is_staff',
        'is_active',
        'is_superuser',
        'role',
    )

    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional information', {
            'fields': (
                'role',
                'gender',
                'birthDate',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
        }),
    )