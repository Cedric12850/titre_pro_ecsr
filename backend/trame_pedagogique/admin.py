from django.contrib import admin
from .models import Competence, SousCompetence, Objectif

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titre', 'est_validee')
    search_fields = ('numero', 'titre')

@admin.register(SousCompetence)
class SousCompetenceAdmin(admin.ModelAdmin):
    list_display = ('lettre', 'titre', 'competence', 'est_validee')
    list_filter = ('competence',)
    search_fields = ('lettre', 'titre')

@admin.register(Objectif)
class ObjectifAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'sous_competence', 'statut')
    list_filter = ('statut', 'sous_competence')
    search_fields = ('intitule',)
