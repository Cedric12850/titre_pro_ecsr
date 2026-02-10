from django.db import models
from django.urls import reverse
from trame_pedagogique.models import Objectif as TrameObjectif
# --- AUTO-CREATION DES OBJECTIFS POUR CHAQUE ELEVE ---
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Eleve(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    date_inscription = models.DateField(auto_now_add=True)
    neph = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Progression(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name="progressions")
    date_cours = models.DateField()
    heure_cours = models.TimeField(null=True, blank=True)
    commentaire = models.TextField(blank=True)
    valide = models.BooleanField(default=False)

    def __str__(self):
        if self.heure_cours:
            return f"{self.eleve} - {self.date_cours} {self.heure_cours}"
        return f"{self.eleve} - {self.date_cours}"
    
    def get_absolute_url(self):
        return reverse("eleves:eleve-detail", kwargs={"pk": self.eleve.pk})
    
class Competence(models.Model):
    nom = models.CharField(max_length=255)
    STATUT_CHOICES = [
        ("ABORDE", "Abordé"),
        ("EN_COURS", "En cours d’acquisition"),
        ("ACQUIS", "Acquis"),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="ABORDE")

    def __str__(self):
        return self.nom

    def update_statut(self):
        """
        Met à jour le statut de la compétence selon les sous-compétences.
        """
        scs = self.sous_competences.all()
        if not scs.exists() or scs.filter(statut="ABORDE").exists():
            self.statut = "ABORDE"
        elif scs.filter(statut="EN_COURS").exists():
            self.statut = "EN_COURS"
        elif all(sc.statut == "ACQUIS" for sc in scs):
            self.statut = "ACQUIS"
        self.save()

class SousCompetence(models.Model):
    nom = models.CharField(max_length=255)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name="sous_competences")
    
    STATUT_CHOICES = [
        ("ABORDE", "Abordé"),
        ("EN_COURS", "En cours d’acquisition"),
        ("ACQUIS", "Acquis"),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="ABORDE")

    def __str__(self):
        return f"{self.nom} ({self.competence.nom})"

    def update_statut(self):
        """
        Met à jour le statut de la sous-compétence selon ses objectifs.
        """
        objectifs = self.objectifs.all()
        if not objectifs.exists() or objectifs.filter(statut="ABORDE").exists():
            self.statut = "ABORDE"
        elif objectifs.filter(statut="EN_COURS").exists():
            self.statut = "EN_COURS"
        elif all(obj.statut == "ACQUIS" for obj in objectifs):
            self.statut = "ACQUIS"
        self.save()

        # Met à jour la compétence parent
        self.competence.update_statut()

class Objectif(models.Model):
    sous_competence = models.ForeignKey(SousCompetence, on_delete=models.CASCADE, related_name="objectifs")
    nom = models.CharField(max_length=255)
    
    STATUT_CHOICES = [
        ("ABORDE", "Abordé"),
        ("EN_COURS", "En cours d’acquisition"),
        ("ACQUIS", "Acquis"),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="ABORDE")

    def __str__(self):
        return f"{self.nom} ({self.sous_competence.nom})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Met à jour le statut de la sous-compétence parent
        self.sous_competence.update_statut()
        

class ProgressionObjectif(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name="progression_objectifs")
    objectif = models.ForeignKey(
        TrameObjectif,
        on_delete=models.CASCADE,
        related_name="progressions_eleves"
    )
    statut = models.CharField(
        max_length=20,
        choices=TrameObjectif.STATUTS,
        default="pas_aborde"
    )
    date = models.DateField(auto_now=True)