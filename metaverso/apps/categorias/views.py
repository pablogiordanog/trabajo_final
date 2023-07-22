from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView

from .models import Categoria

# Create your views here.
class AddCategory(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'categorias/new_category.html'
    success_url = reverse_lazy('apps.categorias:list')
    
    def form_valid(self, form):
        return super().form_valid(form)

class UpdateCategory(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'categorias/update_category.html'
    success_url = reverse_lazy('apps.categorias:list')
    
class DeleteCategory(DeleteView):
    model = Categoria
    template_name = 'categorias/confirm_del.html'
    success_url = reverse_lazy('apps.categorias:list')    

class ListCategory(ListView):
    model = Categoria
    template_name = 'categorias/list.html'
    context_object_name = "categorias"
    
    def get_context_data(self):
        context = super().get_context_data()
        return context
    
    



    