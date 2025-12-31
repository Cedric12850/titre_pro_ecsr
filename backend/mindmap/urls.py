from django.urls import path
from .views import MindMapListView, MindMapCreateView, MindMapUpdateView, MindMapDeleteView

app_name = 'mindmap'

urlpatterns = [
    path('', MindMapListView.as_view(), name='mindmap-list'),               # Liste des cartes
    path('new/', MindMapCreateView.as_view(), name='mindmap-create'),       # Créer une nouvelle carte
    path('editor/<int:pk>/', MindMapUpdateView.as_view(), name='mindmap-edit'),  # Éditer une carte
    path('delete/<int:pk>/', MindMapDeleteView.as_view(), name='mindmap-delete'),# Supprimer
]
