# mindmap/views.py
import json
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MindMap
from django.contrib import messages
from django.views import generic


class MindMapListView(generic.ListView):
    model = MindMap
    template_name = "mindmap/list.html"
    context_object_name = "mindmaps"


class MindMapCreateView(generic.CreateView):
    model = MindMap
    fields = ["title"]
    template_name = "mindmap/editor.html"
    success_url = reverse_lazy("mindmap:mindmap-list")

    def form_valid(self, form):
        raw_data = self.request.POST.get("data")

        if raw_data:
            try:
                data = json.loads(raw_data)

                if self.is_valid_mindmap_data(data):
                    form.instance.data = data

            except (json.JSONDecodeError, TypeError):
                pass

        response = super().form_valid(form)

        messages.success(
            self.request,
            "La carte mentale a été créée avec succès."
        )

        return response

    @staticmethod
    def is_valid_mindmap_data(data):
        """
        Vérifie que les données reçues correspondent
        à une structure mindmap minimale.
        """

        if not isinstance(data, dict):
            return False

        if data.get("format") != "node_tree":
            return False

        if not isinstance(data.get("data"), dict):
            return False

        return True


class MindMapUpdateView(generic.UpdateView):
    model = MindMap
    fields = ["title"]
    template_name = "mindmap/editor.html"
    success_url = reverse_lazy("mindmap:mindmap-list")

    def form_valid(self, form):
        raw_data = self.request.POST.get("data")

        if raw_data:
            try:
                data = json.loads(raw_data)

                if self.is_valid_mindmap_data(data):
                    form.instance.data = data

            except (json.JSONDecodeError, TypeError):
                pass

        response = super().form_valid(form)

        messages.success(
            self.request,
            "La carte mentale a été enregistrée."
        )

        return response

    @staticmethod
    def is_valid_mindmap_data(data):
        if not isinstance(data, dict):
            return False

        if data.get("format") != "node_tree":
            return False

        if not isinstance(data.get("data"), dict):
            return False

        return True


class MindMapDeleteView(generic.DeleteView):
    model = MindMap
    template_name = "mindmap/confirm_delete.html"
    success_url = reverse_lazy("mindmap:mindmap-list")
def abaque_devilliers(request):
    result = None
    if request.method == "POST":
        vitesse = float(request.POST.get("vitesse"))
        mu = float(request.POST.get("mu"))
        g = 9.81
        v_ms = vitesse / 3.6  # conversion km/h -> m/s
        distance = (v_ms ** 2) / (2 * g * mu)
        duree = v_ms / (g * mu)
        result = {
            "vitesse": vitesse,
            "mu": mu,
            "distance": round(distance, 2),
            "duree": round(duree, 2),
        }
    return render(request, "mindmap/abaque.html", {"result": result})

def taux_alcool(request):
    result = None
    if request.method == "POST":
        try:
            masse = float(request.POST.get("masse"))
            sexe = request.POST.get("sexe")  # 'homme' ou 'femme'
            nb_verres = float(request.POST.get("nb_verres"))  # nombre de verres
            beta = float(request.POST.get("beta", 0.15))  # taux d’élimination g/L/h

            # Quantité d'alcool en grammes (10 g par verre standard)
            A = nb_verres * 10

            # Coefficient de diffusion
            r = 0.68 if sexe.lower() == "homme" else 0.55

            # Taux d’alcool immédiat
            TA = A / (r * masse)

            # Temps nécessaire pour éliminer tout l’alcool
            temps_elimination = TA / beta

            result = {
                "masse": masse,
                "sexe": sexe,
                "nb_verres": nb_verres,
                "beta": beta,
                "TA": round(TA, 3),
                "temps_elimination": round(temps_elimination, 2),
            }

        except (ValueError, TypeError):
            result = {"error": "Merci de renseigner correctement tous les champs."}

    return render(request, "mindmap/taux_alcool.html", {"result": result})