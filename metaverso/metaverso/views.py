from django.shortcuts import render
from apps.noticias.models import Noticia

def index(request):
    noticias_recientes = Noticia.objects.order_by('-published')[:3]  # Obtener las 3 noticias más recientes
    return render(request, 'index.html', {'noticias_recientes': noticias_recientes})


def descripcion(request):
    return render(request, 'descripcion.html')


