from django.db import models

class Competence(models.Model):
    NUM_CHOICES = [
        ('C1', 'Compétence 1'),
        ('C2', 'Compétence 2'),
        ('C3', 'Compétence 3'),
        ('C4', 'Compétence 4'),
    ]

    numero = models.CharField(max_length=2, choices=NUM_CHOICES, unique=True)
    titre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} - {self.titre}"

    @property
    def est_validee(self):
        """
        Retourne True si toutes les sous-compétences sont validées.
        Si aucune sous-compétence, retourne False.
        """
        sous_comps = self.souscompetence_set.all()
        if not sous_comps.exists():
            return False
        return all(sc.est_validee for sc in sous_comps)


class SousCompetence(models.Model):
    lettre = models.CharField(max_length=1)  # A, B, C, etc.
    titre = models.CharField(max_length=255)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.competence.numero}{self.lettre} - {self.titre}"

    @property
    def est_validee(self):
        """
        Retourne True si tous les objectifs spécifiques sont validés.
        Si aucun objectif, retourne False.
        """
        objectifs = self.objectif_set.all()
        if not objectifs.exists():
            return False
        return all(obj.statut == 'validee' for obj in objectifs)


class Objectif(models.Model):
    STATUTS = [
        ('pas_aborde', 'Pas encore abordé'),
        ('aborde', 'Abordé'),
        ('en_cours', 'En cours d\'acquisition'),
        ('validee', 'Validée'),
    ]

    sous_competence = models.ForeignKey(SousCompetence, on_delete=models.CASCADE)
    intitule = models.CharField(max_length=255)
    statut = models.CharField(max_length=20, choices=STATUTS, default='pas_aborde')

    def __str__(self):
        return f"{self.sous_competence} - {self.intitule} ({self.get_statut_display()})"
