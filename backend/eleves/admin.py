from django.contrib import admin
from .models import Eleve, Progression

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'date_inscription', 'email', 'telephone')
    search_fields = ('prenom', 'nom', 'email')

@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'date_cours','heure_cours', 'valide')
    list_filter = ('valide', 'date_cours', 'heure_cours')
    ordering = ('date_cours', 'heure_cours')
