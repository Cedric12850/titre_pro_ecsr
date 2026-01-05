from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_ADMIN = "ADMIN"
    ROLE_FORMATEUR = "FORMATEUR"
    ROLE_STAGIAIRE = "STAGIAIRE"
    ROLE_ELEVE = "ELEVE"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Administrateur"),
        (ROLE_FORMATEUR, "Formateur"),
        (ROLE_STAGIAIRE, "Stagiaire"),
        (ROLE_ELEVE, "Élève"),
    ]

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_STAGIAIRE,
    )

    is_approved = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"
