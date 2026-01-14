from django.contrib import admin
from .models import Categorie, ContentBlock, Reglementation, Theme, Sanction


# ────────────── Inlines ──────────────
class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 0


class ReglementationInline(admin.StackedInline):
    model = Reglementation
    extra = 0
    show_change_link = True
    filter_horizontal = ("sanctions",)


# ────────────── Theme ──────────────
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [ContentBlockInline, ReglementationInline]

    list_display = ("title", "categorie", "nb_blocks", "nb_reglementations")
    list_filter = ("categorie", "tags")
    search_fields = ("title",)
    filter_horizontal = ("tags",)
    ordering = ("title",)

    def nb_blocks(self, obj):
        return obj.content_blocks.count() if hasattr(obj, "content_blocks") else 0
    nb_blocks.short_description = "Blocs"

    def nb_reglementations(self, obj):
        return obj.reglementations.count() if hasattr(obj, "reglementations") else 0
    nb_reglementations.short_description = "Réglementations"

    def has_delete_permission(self, request, obj=None):
        return False  # protège les thèmes


# ────────────── Categorie ──────────────
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


# ────────────── Reglementation ──────────────
@admin.register(Reglementation)
class ReglementationAdmin(admin.ModelAdmin):
    list_display = ("lettre", "numero_article", "theme", "retrait_points")
    list_filter = ("lettre", "retrait_points")
    search_fields = ("numero_article",)
    filter_horizontal = ("sanctions",)
    list_select_related = ("theme",)
    ordering = ("lettre", "numero_article")


# ────────────── Sanction ──────────────
@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ("libelle", "duree", "complementaire")
    list_filter = ("libelle", "complementaire")
    search_fields = ("libelle",)
    ordering = ("libelle",)
