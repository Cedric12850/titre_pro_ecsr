from django.urls import path
from .views import (ThemeCreateView,ThemeCustomizeView,ThemeDetailView,ThemeListView, abaque_devilliers, taux_alcool,
)

app_name = 'themes'

urlpatterns = [
    path('add/', ThemeCreateView.as_view(), name='theme-add'),
    path('list/', ThemeListView.as_view(), name='theme-list'),
    path('abaque/', abaque_devilliers, name='abaque'),
    path('taux_alcool/', taux_alcool, name='taux_alcool'),
    path('<slug:slug>/', ThemeDetailView.as_view(), name='theme-detail'),
    path('<slug:slug>/customize/', ThemeCustomizeView.as_view(), name='theme-customize'),
    
]
