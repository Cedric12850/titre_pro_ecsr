from django.urls import path
from . import views

urlpatterns = [
    # Competence URLs
    path('competences/', views.CompetenceListView.as_view(), name='competence_list'),
    path('competences/<int:pk>/', views.CompetenceDetailView.as_view(), name='competence_detail'),

    # SousCompetence URLs
    path('souscompetences/', views.SousCompetenceListView.as_view(), name='souscompetence_list'),
    path('souscompetences/<int:pk>/', views.SousCompetenceDetailView.as_view(), name='souscompetence_detail'),

    # Objectif URLs
    path('objectifs/', views.ObjectifListView.as_view(), name='objectif_list'),
    path('objectifs/<int:pk>/', views.ObjectifDetailView.as_view(), name='objectif_detail'),
]
