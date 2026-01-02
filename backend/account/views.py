# account/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
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
            user.is_approved = False  # compte non validé par l'admin
            user.save()

            # Message flash pour informer l'utilisateur
            messages.success(
                request,
                "Votre compte a été créé avec succès ! Il sera activé après validation par l'administrateur."
            )

            # Optionnel : envoyer un email à l'admin pour validation
            # send_mail(subject, message, from_email, [admin_email], ...)

            return redirect("account:login")
    else:
        form = RegisterForm()

    return render(request, "account/signup.html", {"form": form})