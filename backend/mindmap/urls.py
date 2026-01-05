from django.urls import path
from .views import MindMapListView, MindMapCreateView, MindMapUpdateView, MindMapDeleteView, abaque_devilliers, taux_alcool

app_name = 'mindmap'

urlpatterns = [
    path('', MindMapListView.as_view(), name='mindmap-list'),               # Liste des cartes
    path('new/', MindMapCreateView.as_view(), name='mindmap-create'),       # Créer une nouvelle carte
    path('editor/<int:pk>/', MindMapUpdateView.as_view(), name='mindmap-edit'),  # Éditer une carte
    path('delete/<int:pk>/', MindMapDeleteView.as_view(), name='mindmap-delete'),# Supprimer
    path('abaque/', abaque_devilliers, name='abaque'),
    path('taux_alcool/', taux_alcool, name='taux_alcool'),
]
