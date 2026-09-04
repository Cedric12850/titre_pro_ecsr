from django.contrib import admin
from .models import Categorie, ContentBlock, Reglementation, Theme, Sanction, Livre, Titre, Chapitre


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
        return obj.content_blocks.count()

    nb_blocks.short_description = "Blocs"

    def nb_reglementations(self, obj):
        return obj.reglementations.count()

    nb_reglementations.short_description = "Réglementations"

    def has_delete_permission(self, request, obj=None):
        return False


# ────────────── Categorie ──────────────
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


# ────────────── Livre ──────────────
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ("numero", "titre")
    search_fields = ("titre",)
    ordering = ("numero",)


# ────────────── Titre ──────────────
@admin.register(Titre)
class TitreAdmin(admin.ModelAdmin):
    list_display = ("numero", "titre", "livre")
    list_filter = ("livre",)
    search_fields = ("titre",)
    ordering = ("livre__numero", "numero")


# ────────────── Chapitre ──────────────
@admin.register(Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ("numero", "titre", "get_titre", "get_livre")
    list_filter = ("titre_parent",)  # ✅ OK
    search_fields = ("titre",)
    ordering = ("titre_parent__livre__numero", "titre_parent__numero", "numero")

    def get_titre(self, obj):
        return obj.titre_parent.numero
    get_titre.short_description = "Titre"

    def get_livre(self, obj):
        return obj.titre_parent.livre.numero
    get_livre.short_description = "Livre"

# ────────────── Reglementation ──────────────
@admin.register(Reglementation)
class ReglementationAdmin(admin.ModelAdmin):
    list_display = ("lettre", "numero_article", "theme", "chapitre", "retrait_points")
    list_filter = ("lettre", "retrait_points", "chapitre")
    search_fields = ("numero_article",)
    filter_horizontal = ("sanctions",)
    list_select_related = ("theme", "chapitre")
    ordering = ("lettre", "numero_article")

    autocomplete_fields = ["chapitre"]


# ────────────── Sanction ──────────────
@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ("libelle", "duree", "complementaire")
    list_filter = ("complementaire",) 
    search_fields = ("libelle",)
    ordering = ("libelle",)