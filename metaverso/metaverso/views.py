from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def descripcion(request):
    return render(request, 'descripcion.html')