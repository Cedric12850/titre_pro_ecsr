from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("get_full_name", "email", "role", "is_staff", "is_active", "is_approved")
    list_filter = ("role", "is_staff", "is_active", "is_approved")
    search_fields = ("first_name", "last_name", "email", "username")
    ordering = ("last_name", "first_name")
    readonly_fields = ("last_login", "date_joined")

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Informations personnelles", {"fields": ("first_name", "last_name", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_approved", "groups", "user_permissions")}),
        ("Dates importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "first_name", "last_name", "role", "password1", "password2", "is_active", "is_staff", "is_superuser", "is_approved"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
