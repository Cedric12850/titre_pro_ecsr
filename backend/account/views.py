# account/views.py
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from account.models import User
from .forms import RegisterForm

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authentification avec le modèle User personnalisé
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if not user.is_approved:  # compte non validé par l'admin
                messages.warning(
                    request,
                    "Votre compte est en attente de validation par l’administrateur."
                )
                return render(request, "account/login.html", {"email": email})

            # Connexion réussie
            login(request, user)
            return redirect("home")

        # Identifiants incorrects
        messages.error(request, "Email ou mot de passe incorrect.")
        return render(request, "account/login.html", {"email": email})

    # GET : affichage du formulaire
    return render(request, "account/login.html")

def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.role = User.ROLE_STAGIAIRE  # ou la valeur correcte
            user.save()


            # Email de notification (admin ou utilisateur)
            send_mail(
                subject="Nouvelle inscription ECSR",
                message=(
                    f"Bonjour,\n\n"
                    f"Un nouveau compte vient d’être créé.\n\n"
                    f"Nom : {user.get_full_name()}\n"
                    f"Email : {user.email}\n"
                    f"Rôle : {user.role}\n\n"
                    f"Merci de valider le compte dans l’administration."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["admin@ecsr.fr"],  # ou user.email
                fail_silently=False,
            )

            messages.success(
                request,
                "Votre compte a bien été créé. Il est en attente de validation par un administrateur."
            )
            return redirect("account:login")

    else:
        form = RegisterForm()

    return render(request, "account/signup.html", {"form": form})