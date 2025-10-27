from django.urls import path
from .views import EleveCreateView, EleveListView, EleveDetailView, ProgressionCreateView, ProgressionUpdateView

app_name = 'eleves'

urlpatterns = [
    path('list/', EleveListView.as_view(), name='eleve-list'),
    path('<int:pk>/', EleveDetailView.as_view(), name='eleve-detail'),
    path('<int:pk>/ajouter-progression/', ProgressionCreateView.as_view(), name='progression-create'),
    path('<int:eleve_id>/progression/<int:pk>/modifier/', ProgressionUpdateView.as_view(), name='progression-update'),
    path('ajouter/', EleveCreateView.as_view(), name='eleve-create'),
]
