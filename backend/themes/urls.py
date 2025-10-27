from django import views
from django.urls import path
from .views import ThemeCreateView, ThemeCustomizeView, ThemeDetailView, ThemeListView

app_name = 'themes'

urlpatterns = [
    path('add/', ThemeCreateView.as_view(), name='theme-add'),
    path('list/', ThemeListView.as_view(), name='theme-list'),
    path('<slug:slug>/', ThemeDetailView.as_view(), name='theme-detail'),
    path('<slug:slug>/customize/', ThemeCustomizeView.as_view(), name='theme-customize'),
]
