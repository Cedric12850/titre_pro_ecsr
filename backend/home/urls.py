from django import views
from django.urls import path
from .views import conditions_generales_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path("conditions-generales/", conditions_generales_view, name="cgu"),
]
