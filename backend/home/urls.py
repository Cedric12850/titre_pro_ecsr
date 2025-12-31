from django import views
from django.urls import path
from .views import conditions_generales_view, home_view, login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("conditions-generales/", conditions_generales_view, name="cgu"),
]
