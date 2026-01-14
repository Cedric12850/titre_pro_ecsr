from django import forms
from django.forms import modelformset_factory
from .models import ContentBlock, Reglementation, Theme

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['number', 'title']

class ContentBlockForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = ['title', 'texte', 'image', 'ordre']

class ReglementationForm(forms.ModelForm):
    class Meta:
        model = Reglementation
        fields = ['lettre', 'numero_article', 'date_version', 'contenu', 'amende', 'retrait_points', 'sanctions']
        widgets = {
            'lettre': forms.Select(attrs={'class': 'form-select'}),
            'numero_article': forms.TextInput(attrs={'class': 'form-control'}),
            'date_version': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'amende': forms.TextInput(attrs={'class': 'form-control'}),
            'retrait_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'sanctions': forms.CheckboxSelectMultiple(),
        }
        
ContentBlockFormSet = modelformset_factory(ContentBlock, form=ContentBlockForm, extra=1, can_delete=True)
ReglementationFormSet = modelformset_factory(Reglementation, form=ReglementationForm, extra=1, can_delete=True)
