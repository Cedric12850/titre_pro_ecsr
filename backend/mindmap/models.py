# site_titre_pro_ecsr/mindmap/models.py
from django.db import models


def default_mindmap_data():
    """
    Structure par défaut d'une carte mentale.

    Le format node_tree est utilisé par l'éditeur jsMind.
    """

    return {
        "meta": {
            "name": "Conduct'Art",
            "version": "2.0"
        },
        "format": "node_tree",
        "data": {
            "id": "root",
            "topic": "Nouvelle carte",
            "expanded": True,
            "children": []
        }
    }


class MindMap(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )

    data = models.JSONField(
        default=default_mindmap_data,
        verbose_name="Données de la carte"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Créée le"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Modifiée le"
    )

    class Meta:
        verbose_name = "Carte mentale"
        verbose_name_plural = "Cartes mentales"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
