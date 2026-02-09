from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Competence, SousCompetence, Objectif

# --------------------
# Competence CRUD
# --------------------
class CompetenceListView(ListView):
    model = Competence
    template_name = "trame_pedagogique/competence_list.html"

class CompetenceDetailView(DetailView):
    model = Competence
    template_name = "trame_pedagogique/competence_detail.html"

class CompetenceCreateView(CreateView):
    model = Competence
    fields = ['numero', 'titre']
    template_name = "trame_pedagogique/competence_form.html"
    success_url = reverse_lazy('competence_list')

class CompetenceUpdateView(UpdateView):
    model = Competence
    fields = ['numero', 'titre']
    template_name = "trame_pedagogique/competence_form.html"
    success_url = reverse_lazy('competence_list')

class CompetenceDeleteView(DeleteView):
    model = Competence
    template_name = "trame_pedagogique/competence_confirm_delete.html"
    success_url = reverse_lazy('competence_list')


# --------------------
# SousCompetence CRUD
# --------------------
class SousCompetenceListView(ListView):
    model = SousCompetence
    template_name = "trame_pedagogique/souscompetence_list.html"

class SousCompetenceDetailView(DetailView):
    model = SousCompetence
    template_name = "trame_pedagogique/souscompetence_detail.html"

class SousCompetenceCreateView(CreateView):
    model = SousCompetence
    fields = ['lettre', 'titre', 'competence']
    template_name = "trame_pedagogique/souscompetence_form.html"
    success_url = reverse_lazy('souscompetence_list')

class SousCompetenceUpdateView(UpdateView):
    model = SousCompetence
    fields = ['lettre', 'titre', 'competence']
    template_name = "trame_pedagogique/souscompetence_form.html"
    success_url = reverse_lazy('souscompetence_list')

class SousCompetenceDeleteView(DeleteView):
    model = SousCompetence
    template_name = "trame_pedagogique/souscompetence_confirm_delete.html"
    success_url = reverse_lazy('souscompetence_list')


# --------------------
# Objectif CRUD
# --------------------
class ObjectifListView(ListView):
    model = Objectif
    template_name = "trame_pedagogique/objectif_list.html"

class ObjectifDetailView(DetailView):
    model = Objectif
    template_name = "trame_pedagogique/objectif_detail.html"

class ObjectifCreateView(CreateView):
    model = Objectif
    fields = ['sous_competence', 'intitule', 'statut']
    template_name = "trame_pedagogique/objectif_form.html"
    success_url = reverse_lazy('objectif_list')

class ObjectifUpdateView(UpdateView):
    model = Objectif
    fields = ['sous_competence', 'intitule', 'statut']
    template_name = "trame_pedagogique/objectif_form.html"
    success_url = reverse_lazy('objectif_list')

class ObjectifDeleteView(DeleteView):
    model = Objectif
    template_name = "trame_pedagogique/objectif_confirm_delete.html"
    success_url = reverse_lazy('objectif_list')

# Create your views here.
