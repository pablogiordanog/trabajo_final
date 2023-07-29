from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView

from .models import Noticia, Categoria, Comentario
from .forms import FormNotice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.utils import timezone
from .forms import AddNoticeForm 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
class AddNotice(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = AddNoticeForm  
    template_name = 'noticias/new_notice.html'
    success_url = reverse_lazy('apps.noticias:list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.published = timezone.now()
        return super().form_valid(form)

class UpdateNotice(LoginRequiredMixin, UpdateView):
    model = Noticia
    fields = ['id','titulo','autor','descripcion','published','imagen','categoria']
    template_name = 'noticias/update_notice.html'
    success_url = reverse_lazy('apps.noticias:list')
    
class DeleteNotice(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'noticias/confirm_del.html'
    success_url = reverse_lazy('apps.noticias:list')    
    
    

class ListNotice(ListView):
    model = Noticia
    template_name = 'noticias/list.html'
    context_object_name = "noticias"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        noticias = context['noticias']
        paginator = Paginator(noticias, 6)  

        page = self.request.GET.get('page')
        try:
            noticias_paginadas = paginator.page(page)
        except PageNotAnInteger:
            noticias_paginadas = paginator.page(1)
        except EmptyPage:
            noticias_paginadas = paginator.page(paginator.num_pages)

        context['noticias'] = noticias_paginadas
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria_id')

        if categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            queryset = queryset.filter(categoria=categoria)

        query = self.request.GET.get('buscador')
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        
        orden = self.request.GET.get('orden')
        if orden == 'fecha':
            queryset = queryset.order_by('published')  # Ordenar por fecha
        elif orden == 'titulo':
            queryset = queryset.order_by('titulo')  # Ordenar por título

        return queryset


class AddCategory(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'noticias/new_category.html'
    success_url = reverse_lazy('apps.noticias:add_notice')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
def agregar_comentario(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido')

        if contenido:
            # Obtener el usuario actualmente autenticado
            autor = request.user.username  # Puedes usar el nombre de usuario o el nombre completo del usuario
            comentario = Comentario(noticia=noticia, autor=autor, contenido=contenido)
            comentario.save()
    
    return redirect('apps.noticias:detail', pk=noticia_id)



class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia.html'
    context_object_name = 'noticia'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comentarios = self.object.comentarios.all()
        print(comentarios)  # Agregar esta línea para imprimir los comentarios
        context['comentarios'] = comentarios
        return context
    
    
    
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        comentario.delete()
    return redirect('apps.noticias:detail', pk=comentario.noticia.pk)





class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'noticias/delete_category.html'
    success_url = reverse_lazy('apps.noticias:list')

    def delete(self, request, *args, **kwargs):
        # Obtener la categoría que se va a eliminar
        categoria = self.get_object()

        # Eliminar todas las noticias asociadas a la categoría
        noticias = Noticia.objects.filter(categoria=categoria)
        noticias.delete()

        # Llamar al método delete() de la clase base para eliminar la categoría
        return super().delete(request, *args, **kwargs)