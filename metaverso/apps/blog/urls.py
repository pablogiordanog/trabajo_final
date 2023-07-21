from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 
from django.contrib.auth.views import LogoutView




urlpatterns = [
    
    path('noticias/', views.noticias, name='noticias'),
    path('registro', views.login_or_register, name='registro'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)