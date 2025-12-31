from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages


def home_view(request):
    return render(request, 'home/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # rediriger selon le rôle
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    else:
        form = LoginForm()
    return render(request, 'home/login.html',{"form": form, "hide_header": True})

def logout_view(request):
    logout(request)
    return redirect('login')

def conditions_generales_view(request):
    return render(request, "home/conditions_generales.html")
