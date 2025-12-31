from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EleveForm, ProgressionForm
from .models import Eleve, Progression
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from datetime import date


class EleveListView(ListView):
    model = Eleve
    template_name = 'eleves/eleve_list.html'
    context_object_name = 'eleves'
    
    def get_queryset(self):
        qs = super().get_queryset()
        sort = self.request.GET.get('sort', 'nom_asc')  # valeur par défaut
        if sort == 'nom_asc':
            qs = qs.order_by('nom', 'prenom')
        elif sort == 'nom_desc':
            qs = qs.order_by('-nom', '-prenom')
        elif sort == 'date_asc':
            qs = qs.order_by('date_inscription')
        elif sort == 'date_desc':
            qs = qs.order_by('-date_inscription')
        return qs


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
    
class EleveDeleteView(DeleteView):
    model = Eleve
    template_name = 'eleves/eleve_confirm_delete.html'  # page de confirmation
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
    
def eleve_progression_pdf(request, pk):
    eleve = Eleve.objects.get(pk=pk)
    progressions = eleve.progressions.all().order_by("date_cours", "heure_cours")

    html_string = render_to_string(
        "eleves/eleve_pdf_progression.html",
        {
            "eleve": eleve,
            "progressions": progressions,
            "date": date.today(),
        }
    )

    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = (
        f'inline; filename="progression_{eleve.nom}_{eleve.prenom}.pdf"'
    )
    return response
