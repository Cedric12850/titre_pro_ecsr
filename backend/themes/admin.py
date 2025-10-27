from django.contrib import admin
from .models import Categorie, ContentBlock, Reglementation, Theme, Sanction


class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 6


class ReglementationInline(admin.StackedInline):  # ← important !
    model = Reglementation
    extra = 1
    filter_horizontal = ('sanctions',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [ContentBlockInline, ReglementationInline]
    list_display = ('title',)
    filter_horizontal = ('tags',)
    

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Reglementation)
class ReglementationAdmin(admin.ModelAdmin):
    list_display = ('lettre', 'numero_article',)
    filter_horizontal = ('sanctions',)
    list_filter = ('lettre','retrait_points',)


@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ('duree','libelle','complementaire')
    list_filter = ('libelle','complementaire',)
