from django.contrib import admin
from .models import Eleve, Progression, Competence, SousCompetence, Objectif, ProgressionObjectif

# ────────────── Eleve ──────────────
@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ("prenom", "nom", "date_inscription", "email", "telephone")
    search_fields = ("prenom", "nom", "email")
    list_filter = ("date_inscription",)
    ordering = ("nom", "prenom")


# ────────────── Progression ──────────────
@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ("eleve", "date_cours", "heure_cours", "valide")
    list_filter = ("valide", "date_cours", "heure_cours")
    search_fields = ("eleve__prenom", "eleve__nom")
    ordering = ("date_cours", "heure_cours")
    autocomplete_fields = ("eleve",)
    list_select_related = ("eleve",)


# ────────────── Competence / SousCompetence / Objectif ──────────────

class SousCompetenceInline(admin.TabularInline):
    model = SousCompetence
    extra = 0
    fields = ('nom', 'statut')
    readonly_fields = ('statut',)


class ObjectifInline(admin.TabularInline):
    model = Objectif
    extra = 0
    fields = ('nom', 'statut')
    readonly_fields = ('statut',)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut')
    inlines = [SousCompetenceInline]
    search_fields = ('nom',)


@admin.register(SousCompetence)
class SousCompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'competence', 'statut')
    search_fields = ('nom', 'competence__nom')
    list_filter = ('competence', 'statut')
    inlines = [ObjectifInline]


@admin.register(Objectif)
class ObjectifAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sous_competence', 'statut')
    search_fields = ('nom', 'sous_competence__nom')
    list_filter = ('sous_competence__competence', 'statut')