from django.contrib import admin
from .models import Eleve, Progression


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
