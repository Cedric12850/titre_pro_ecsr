from django import forms
from .models import Eleve, Progression
from ckeditor.widgets import CKEditorWidget

class ProgressionForm(forms.ModelForm):
    commentaire = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Progression
        fields = ['date_cours','heure_cours', 'commentaire', 'valide']
        widgets = {
            'date_cours': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_cours': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'valide': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'date_naissance', 'neph', 'email', 'telephone']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }