import random
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from account.mixins import RoleRequiredMixin
from .models import Categorie, ContentBlock, Reglementation, Theme
from .forms import ContentBlockFormSet, ReglementationFormSet, ThemeForm

class ThemeCreateView(CreateView):
    model = Theme
    form_class = ThemeForm
    template_name = 'themes/theme_add.html'
    success_url = reverse_lazy('themes:theme-list')  # Redirige vers la même page après création
    
    
class ThemeListView(ListView):
    model = Theme
    template_name = 'themes/theme_list.html'
    context_object_name = 'themes'
    
    # Liste provisoire de stagiaires
    STAGIAIRES = [
        {"prenom": "Caroline"},
        {"prenom": "Célia"},
        {"prenom": "Laure"},
        {"prenom": "Patricia"},
        {"prenom": "Frédéric"},
        {"prenom": "Raphael"},
        {"prenom": "Valentin"},
    ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        
        # --- Choix aléatoire d’un thème ---
        if "choisir" in self.request.GET:
            # Récupérer tous les thèmes disponibles
            themes = list(Theme.objects.all())
            if themes:
                # Tirer un thème au hasard
                theme_choisi = random.choice(themes)
                context['theme_aleatoire'] = theme_choisi
            
        # Choix aléatoire d’un stagiaire
        if "choisir_eleve" in self.request.GET and self.STAGIAIRES:
            context['eleve_aleatoire'] = random.choice(self.STAGIAIRES)
            
        return context
    
class ThemeDetailView(DetailView):
    model = Theme
    template_name = 'themes/theme_detail.html'
    context_object_name = 'theme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_blocks'] = self.object.content_blocks.all()
        context['reglementations'] = self.object.reglementations.all()
        return context
    
class ThemeCustomizeView(RoleRequiredMixin, View):
    allowed_roles = ["ADMIN", "FORMATEUR"]
    def get(self, request, slug):
        theme = get_object_or_404(Theme, slug=slug)
        contentblock_formset = ContentBlockFormSet(
            queryset=ContentBlock.objects.filter(theme=theme),
            prefix='contentblock'
        )
        reglementation_formset = ReglementationFormSet(
            queryset=Reglementation.objects.filter(theme=theme),
            prefix='reglementation'
        )
        return render(request, 'themes/theme_customize.html', {
            'theme': theme,
            'contentblock_formset': contentblock_formset,
            'reglementation_formset': reglementation_formset,
        })

    def post(self, request, slug):
        theme = get_object_or_404(Theme, slug=slug)
        contentblock_formset = ContentBlockFormSet(
            request.POST,
            request.FILES,
            queryset=ContentBlock.objects.filter(theme=theme),
            prefix='contentblock'
        )
        reglementation_formset = ReglementationFormSet(
            request.POST,
            queryset=Reglementation.objects.filter(theme=theme),
            prefix='reglementation'
        )

        if contentblock_formset.is_valid() and reglementation_formset.is_valid():
            # Sauvegarder les ContentBlocks
            contentblocks = contentblock_formset.save(commit=False)
            for cb in contentblocks:
                cb.theme = theme
                cb.save()
            for cb_del in contentblock_formset.deleted_objects:
                cb_del.delete()

            # Sauvegarder les Reglementations
            reglementations = reglementation_formset.save(commit=False)
            for reg in reglementations:
                reg.theme = theme
                reg.save()
            for reg_del in reglementation_formset.deleted_objects:
                reg_del.delete()

            return redirect('themes:theme-detail', slug=theme.slug)

        # En cas d'erreur, réafficher les formulaires avec les erreurs
        return render(request, 'themes/theme_customize.html', {
            'theme': theme,
            'contentblock_formset': contentblock_formset,
            'reglementation_formset': reglementation_formset,
        })
