from django.db import models
from django.urls import reverse

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