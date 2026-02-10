from trame_pedagogique.models import Objectif
from .models import ProgressionObjectif, Eleve

def init_progression_objectifs(eleve: Eleve):
    for obj in Objectif.objects.all():
        ProgressionObjectif.objects.get_or_create(
            eleve=eleve,
            objectif=obj,
            defaults={'statut': 'pas_aborde'}
        )