from django.db import models
from django.utils.text import slugify

class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name

class Theme(models.Model):
    number = models.PositiveBigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    # CATEGORIE PRINCIPALE (exclusif)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='themes_principaux'
    )

    # TAGS (multiples)
    tags = models.ManyToManyField(
        Categorie,
        blank=True,
        related_name='themes_tags'
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            base = f"{self.number}-{self.title}"
            self.slug = slugify(base)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Thème {self.number} – {self.title}"
    

class ContentBlock(models.Model):
    theme = models.ForeignKey(Theme, related_name='content_blocks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)  # titre optionnel
    texte = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='themes/content_images/', blank=True, null=True)
    ordre = models.PositiveIntegerField(default=0)  # ordre pour le tri

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return f"{self.theme.title} - Bloc {self.ordre} - {self.title or 'Sans titre'}"
    
class Sanction(models.Model):
    libelle = models.CharField(max_length=255, help_text="Nom de la sanction, ex: Suspension de permis")
    duree = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Durée de la sanction (ex: 3 ans, 6 mois, définitif)"
    )
    complementaire = models.BooleanField(default=False, help_text="Cochez si c’est une sanction complémentaire")

    def __str__(self):
        return f"{self.libelle} ({self.duree})" if self.duree else self.libelle
    
class Reglementation(models.Model):
    LETTRE_CHOICES = [
        ('L', 'L'),
        ('R', 'R'),
    ]
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="reglementations", blank=True, null=True)
    lettre = models.CharField(max_length=1, choices=LETTRE_CHOICES)
    numero_article = models.CharField(max_length=10)  # ex: '111-1'
    date_version = models.DateField()
    contenu = models.TextField()
    amende = models.TextField(blank=True, null=True)
    retrait_points = models.PositiveIntegerField(default=0)
    sanctions = models.ManyToManyField('Sanction', blank=True, related_name="reglementations")

    def __str__(self):
        return f"Article {self.lettre} {self.numero_article}"
