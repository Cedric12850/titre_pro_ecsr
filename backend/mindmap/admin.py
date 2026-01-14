from django.contrib import admin
from .models import MindMap

@admin.register(MindMap)
class MindMapAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    # Si tu ajoutes un jour owner :
    # autocomplete_fields = ("owner",)
    # list_select_related = ("owner",)
