from django.shortcuts import render


def home_view(request):
    return render(request, 'home/index.html')

def conditions_generales_view(request):
    return render(request, "home/conditions_generales.html")
