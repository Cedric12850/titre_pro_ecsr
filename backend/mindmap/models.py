# site_titre_pro_ecsr/mindmap/models.py
from django.db import models

def default_mindmap_data():
    return {
        "meta": {
            "name": "mindmap",
            "version": "1.0"
        },
        "format": "node_array",
        "data": [
            {
                "id": "root",
                "isroot": True,
                "topic": "Nouvelle carte"
            }
        ]
    }


class MindMap(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)  # plus tard
    title = models.CharField(max_length=200)
    data = models.JSONField(default=default_mindmap_data)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
