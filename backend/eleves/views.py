from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import EleveForm, ProgressionForm
from .models import Eleve, Progression

class EleveListView(ListView):
    model = Eleve
    template_name = 'eleves/eleve_list.html'
    context_object_name = 'eleves'


class EleveDetailView(DetailView):
    model = Eleve
    template_name = 'eleves/eleve_detail.html'
    context_object_name = 'eleve'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On ajoute toutes les progressions de l'élève courant
        context['progressions'] = self.object.progressions.all()
        return context
    

class EleveCreateView(CreateView):
    model = Eleve
    form_class = EleveForm
    template_name = 'eleves/eleve_form.html'
    success_url = reverse_lazy('eleves:eleve-list')


class ProgressionCreateView(CreateView):
    model = Progression
    form_class = ProgressionForm
    template_name = 'eleves/progression_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eleve = Eleve.objects.get(pk=self.kwargs.get('pk'))
        context['eleve'] = eleve
        return context

    def form_valid(self, form):
        # associer automatiquement la progression à l'élève
        eleve = Eleve.objects.get(pk=self.kwargs.get('pk'))
        form.instance.eleve = eleve
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("eleves:eleve-detail", kwargs={"pk": self.kwargs["pk"]})

class ProgressionUpdateView(UpdateView):
    model = Progression
    form_class = ProgressionForm
    template_name = 'eleves/progression_form.html'

    def get_success_url(self):
        return reverse_lazy("eleves:eleve-detail", kwargs={"pk": self.object.eleve.pk})