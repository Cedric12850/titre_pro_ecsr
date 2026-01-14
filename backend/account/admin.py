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

    # ─────────────── Dashboard rapide ───────────────
    change_list_template = "admin/accounts/user/change_list.html"

    def changelist_view(self, request, extra_context=None):
        # Comptage par rôle et non approuvés
        total_users = User.objects.count()
        count_admin = User.objects.filter(role=User.ROLE_ADMIN).count()
        count_formateur = User.objects.filter(role=User.ROLE_FORMATEUR).count()
        count_stagiaire = User.objects.filter(role=User.ROLE_STAGIAIRE).count()
        count_eleve = User.objects.filter(role=User.ROLE_ELEVE).count()
        count_non_approved = User.objects.filter(is_approved=False).count()

        extra_context = extra_context or {}
        extra_context.update({
            "total_users": total_users,
            "count_admin": count_admin,
            "count_formateur": count_formateur,
            "count_stagiaire": count_stagiaire,
            "count_eleve": count_eleve,
            "count_non_approved": count_non_approved,
        })
        return super().changelist_view(request, extra_context=extra_context)
