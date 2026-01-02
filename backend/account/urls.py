from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup_view

app_name = "account"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),
]
