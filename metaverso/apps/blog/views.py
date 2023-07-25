# Create your views here.
from django.shortcuts import render
from.models import Usuarios
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistroForm


def noticias(request):
    return render(request, 'noticias.html')


def login_or_register(request):  #VISTA DE LOGIN Y REGISTRO 
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        register_form = RegistroForm(data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('apps.noticias:list')  # Redireccionar a la página de noticias después del inicio de sesión.
        elif register_form.is_valid():
            user = register_form.save(commit=False)
            if 'imagen' in request.FILES:
                user.imagen = request.FILES['imagen']
            user.save()
            login(request, user)
            return redirect('inicio')# Redireccionar a la página de inicio después del registro.
        
    else:
        login_form = AuthenticationForm()
        register_form = RegistroForm()

    return render(request, 'registro.html', {'login_form': login_form, 'register_form': register_form})



def ListarUsuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'listar_usuarios.html'
    contexto = {
        "usuarios": usuarios
    }
    return render(request, template_name, contexto)


class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = 'confirma_eliminar.html'
    success_url = reverse_lazy('listar')
    
    
class editar_perfil(LoginRequiredMixin, UpdateView):
    model = Usuarios
    fields = ['first_name','last_name','username','fecha_nacimiento', 'email', 'imagen']
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('listar')