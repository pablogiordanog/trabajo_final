from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView

from .models import Noticia, Categoria
from .forms import FormNotice

# Create your views here.
class AddNotice(CreateView):
    model = Noticia
    fields = ['titulo', 'autor', 'descripcion', 'published', 'imagen', 'categoria']
    template_name = 'noticias/new_notice.html'
    success_url = reverse_lazy('apps.noticias:list')
    
    def form_valid(self, form):
        #form.instance.colaborador = self.request.user
        return super().form_valid(form)

class UpdateNotice(UpdateView):
    model = Noticia
    fields = ['id','titulo','autor','descripcion','published','imagen','categoria']
    template_name = 'noticias/update_notice.html'
    success_url = reverse_lazy('apps.noticias:list')
    
class DeleteNotice(DeleteView):
    model = Noticia
    template_name = 'noticias/confirm_del.html'
    success_url = reverse_lazy('apps.noticias:list')    

class ListNotice(ListView):
    model = Noticia
    template_name = 'noticias/list.html'
    context_object_name = "noticias"
    # -----Paginación------
    #paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')

def ListaNoticeForCategory(request, categoria):
    categorias2 = Categoria.objects.filter(nombre=categoria)
    noticias = Noticia.objects.filter(
        categoria=categorias2[0].id).order_by('published')
    categorias = Categoria.objects.all()
    template_name = 'noticias/list.html'
    contexto = {
        'noticias': noticias,
        'categorias': categorias
    }
    return render(request, template_name, contexto)


def order_notice_for_category(request):
    # Obtener el parámetro 'orden' de la URL(para eso en html debe haber un elemento con name='orden' y un valor(value=''))
    orden = request.GET.get('orden', '')
    # Validamos lo que contiene value
    print(orden)
    if orden == 'fecha':
        # Ordenar por fecha(Si quisiera desc seria: ('-published'))
        notices = Noticia.objects.order_by('published')
    elif orden == 'titulo':
        # Ordenar por título(Si quisiera desc seria: ('-titulo'))
        notices = Noticia.objects.order_by('titulo')
        print('entro en titulo')
        print(notices)
    else:  # Si no hay nada solo todos sin orden
        notices = Noticia.objects.all()  # Obtener todos las noticias sin ordenar

    context = {
        'noticias': notices,
    }
    return render(request, 'noticias/list.html', context)


def notice_details(request, id):
    notice = Noticia.objects.get(id=id)
    form = FormNotice(request.POST)

    if form.is_valid():
        #if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.notice = notice
            aux.save()
            form = FormNotice()
        #else:
        #    return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'notice': notice,
        'form': form,
    }
    template_name = 'noticias/notice.html'
    return render(request, template_name, contexto)
    