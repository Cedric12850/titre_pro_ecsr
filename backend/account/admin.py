from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "role", "is_approved")
    list_filter = ("role", "is_approved")
    actions = ["approve_users"]

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True, is_active=True)

    approve_users.short_description = "Valider les comptes sélectionnés"
