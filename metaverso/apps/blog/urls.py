from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 
from django.contrib.auth.views import LogoutView

from .views import EliminarUsuario
from .views import editar_perfil


urlpatterns = [
    
    path('noticias/', views.noticias, name='noticias'),
    path('registro', views.login_or_register, name='registro'),
    path('listar',views.ListarUsuarios, name='listar'),
    path("eliminar_usuario/<int:pk>",
         EliminarUsuario.as_view(), name='eliminar_usuario'),
    path("editar_perfil/<int:pk>",
         editar_perfil.as_view(), name='editar_perfil'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)