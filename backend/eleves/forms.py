from django import forms
from .models import Eleve, Progression, ProgressionObjectif
from ckeditor.widgets import CKEditorWidget
from django.forms import modelformset_factory

ProgressionObjectifFormSet = modelformset_factory(
    ProgressionObjectif,
    fields=['statut'],
    extra=0
)

class ProgressionForm(forms.ModelForm):
    commentaire = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Progression
        fields = ['date_cours', 'heure_cours', 'commentaire', 'valide']
        widgets = {
            'date_cours': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date', 'class': 'form-control'}),
            'heure_cours': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'valide': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'date_naissance', 'neph', 'email', 'telephone']
        widgets = {
            'date_naissance': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }
        
