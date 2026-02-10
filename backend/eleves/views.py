from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.http import HttpResponse
from django.template.loader import render_to_string

from trame_pedagogique.models import Competence, SousCompetence, Objectif as TrameObjectif
from weasyprint import HTML
from datetime import date

from account.mixins import RoleRequiredMixin

from .forms import EleveForm, ProgressionForm, ProgressionObjectifFormSet
from .models import Eleve, Progression, ProgressionObjectif



class EleveListView(RoleRequiredMixin, ListView):
    model = Eleve
    template_name = 'eleves/eleve_list.html'
    context_object_name = 'eleves'
    allowed_roles = ["ADMIN", "FORMATEUR", "STAGIAIRE"]

    def get_queryset(self):
        qs = super().get_queryset()
        sort = self.request.GET.get('sort', 'nom_asc')

        if sort == 'nom_asc':
            qs = qs.order_by('nom', 'prenom')
        elif sort == 'nom_desc':
            qs = qs.order_by('-nom', '-prenom')
        elif sort == 'date_asc':
            qs = qs.order_by('date_inscription')
        elif sort == 'date_desc':
            qs = qs.order_by('-date_inscription')

        return qs

class EleveDetailView(RoleRequiredMixin, DetailView):
    model = Eleve
    template_name = 'eleves/eleve_detail.html'
    context_object_name = 'eleve'
    allowed_roles = ["ADMIN", "FORMATEUR", "STAGIAIRE"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eleve = self.object

        # ✅ Récupère uniquement les progressions réelles avec commentaire
        context['progressions'] = eleve.progressions.all()  # ou le related_name exact de ton modèle

        # Récupère les compétences C1 à C4 et leur statut
        competences = Competence.objects.order_by('numero')
        competence_data = []

        for comp in competences:
            sous_comps = SousCompetence.objects.filter(competence=comp).order_by('lettre')
            sc_list = []
            comp_statuts = []

            for sc in sous_comps:
                objs = ProgressionObjectif.objects.filter(
                    eleve=eleve,
                    objectif__sous_competence=sc
                ).select_related('objectif')

                if not objs.exists():
                    sc_statut = "pas_aborde"
                elif any(o.statut == "en_cours" for o in objs):
                    sc_statut = "en_cours"
                elif all(o.statut == "validee" for o in objs):
                    sc_statut = "validee"
                elif any(o.statut == "aborde" for o in objs):
                    sc_statut = "aborde"
                else:
                    sc_statut = "pas_aborde"

                sc_list.append({
                    'sous_competence': sc,
                    'objectifs': objs,
                    'statut': sc_statut
                })
                comp_statuts.append(sc_statut)

            if all(s == "validee" for s in comp_statuts):
                comp_statut = "validee"
            elif any(s == "en_cours" for s in comp_statuts):
                comp_statut = "en_cours"
            elif any(s == "aborde" for s in comp_statuts):
                comp_statut = "aborde"
            else:
                comp_statut = "pas_aborde"

            competence_data.append({
                'competence': comp,
                'sous_competences': sc_list,
                'statut': comp_statut
            })

        context['competence_data'] = competence_data
        return context

class EleveCreateView(RoleRequiredMixin, CreateView):
    model = Eleve
    form_class = EleveForm
    template_name = 'eleves/eleve_form.html'
    success_url = reverse_lazy('eleves:eleve-list')
    allowed_roles = ["ADMIN", "FORMATEUR"]

    def form_valid(self, form):
        response = super().form_valid(form)
        eleve = self.object

        # On récupère tous les objectifs existants dans la trame pédagogique
        from trame_pedagogique.models import Objectif as TrameObjectif
        from .models import ProgressionObjectif

        objectifs = TrameObjectif.objects.all()
        if objectifs.exists():
            objs_to_create = [
                ProgressionObjectif(
                    eleve=eleve,
                    objectif=obj,
                    statut="pas_aborde"
                )
                for obj in objectifs
            ]
            ProgressionObjectif.objects.bulk_create(objs_to_create)
            print(f"{len(objs_to_create)} ProgressionObjectif créés pour l'élève {eleve}")
        else:
            print("Aucun objectif trouvé dans la trame pédagogique !")

        return response

    
class EleveDeleteView(RoleRequiredMixin, DeleteView):
    model = Eleve
    template_name = 'eleves/eleve_confirm_delete.html'
    success_url = reverse_lazy('eleves:eleve-list')
    allowed_roles = ["ADMIN"]


class ProgressionCreateView(RoleRequiredMixin, CreateView):
    model = Progression
    form_class = ProgressionForm
    template_name = 'eleves/progression_form.html'
    allowed_roles = ["ADMIN", "FORMATEUR","STAGIAIRE"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eleve'] = get_object_or_404(Eleve, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.eleve = get_object_or_404(Eleve, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "eleves:eleve-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )

class ProgressionUpdateView(RoleRequiredMixin, UpdateView):
    model = Progression
    form_class = ProgressionForm
    template_name = 'eleves/progression_form.html'
    allowed_roles = ["ADMIN", "FORMATEUR", "STAGIAIRE"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["eleve"] = self.object.eleve
        return context

    def get_success_url(self):
        return reverse_lazy(
            "eleves:eleve-detail",
            kwargs={"pk": self.object.eleve.pk}
        )

    
def eleve_progression_pdf(request, pk):
    if not request.user.is_authenticated or request.user.role not in ["ADMIN", "FORMATEUR"]:
        return HttpResponse("Accès refusé", status=403)

    eleve = get_object_or_404(Eleve, pk=pk)
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

def eleve_objectifs_update(request, eleve_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)

    # 1️⃣ Initialiser les objectifs manquants pour cet élève
    for obj in TrameObjectif.objects.all():
        ProgressionObjectif.objects.get_or_create(
            eleve=eleve,
            objectif=obj,
            defaults={'statut': 'pas_aborde'}
        )

    # 2️⃣ Récupérer tous les ProgressionObjectif pour cet élève
    qs = ProgressionObjectif.objects.filter(eleve=eleve).select_related(
        "objectif",
        "objectif__sous_competence",
        "objectif__sous_competence__competence"
    )

    # 3️⃣ Mettre à jour les statuts si POST
    if request.method == "POST":
        for obj in qs:
            field_name = f"form-{obj.id}"  # correspond au name du <select>
            new_statut = request.POST.get(field_name)
            if new_statut and new_statut != obj.statut:
                obj.statut = new_statut
                obj.save()
        return redirect('eleves:eleve-objectifs-update', eleve_id=eleve.id)

    # 4️⃣ Préparer les données pour le template avec statuts calculés
    competence_data = []
    for comp in Competence.objects.order_by("numero"):
        sous_comps = SousCompetence.objects.filter(competence=comp).order_by("lettre")
        sc_list = []
        for sc in sous_comps:
            objs = qs.filter(objectif__sous_competence=sc)

            # 🔹 Calcul du statut de la sous-compétence pour cet élève
            if not objs.exists() or all(o.statut == "pas_aborde" for o in objs):
                sc_statut = "pas_aborde"
            elif any(o.statut == "en_cours" for o in objs):
                sc_statut = "en_cours"
            elif all(o.statut == "validee" for o in objs):
                sc_statut = "validee"
            else:
                sc_statut = "aborde"  # par défaut

            sc_list.append({
                "sous_competence": sc,
                "statut": sc_statut,
                "objectifs": objs
            })

        # 🔹 Calcul du statut de la compétence selon les sous-compétences
        sc_statuts = [sc["statut"] for sc in sc_list]
        if not sc_statuts or all(s == "pas_aborde" for s in sc_statuts):
            comp_statut = "pas_aborde"
        elif any(s == "en_cours" for s in sc_statuts):
            comp_statut = "en_cours"
        elif all(s == "validee" for s in sc_statuts):
            comp_statut = "validee"
        else:
            comp_statut = "aborde"

        competence_data.append({
            "competence": comp,
            "statut": comp_statut,
            "sous_competences": sc_list
        })

    return render(request, "eleves/eleve_objectifs_form.html", {
        "eleve": eleve,
        "competence_data": competence_data,
    })