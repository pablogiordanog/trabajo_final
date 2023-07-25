from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from .views import ListNotice,AddNotice, UpdateNotice, DeleteNotice,AddCategory, NoticiaDetailView, eliminar_comentario, agregar_comentario

app_name = 'apps.noticias'

urlpatterns = [
    path('list/', ListNotice.as_view(), name='list'),
    
    path("add_notice/", AddNotice.as_view(), name='add_notice'),
    path("update_notice/<int:pk>",
         UpdateNotice.as_view(), name='update_notice'),
    path("delete_notice/<int:pk>", DeleteNotice.as_view(), name='delete_notice'),
    path("add_category/", AddCategory.as_view(), name='add_category'),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='detail'),
    path('noticia/<int:noticia_id>/agregar_comentario/', agregar_comentario, name='agregar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'),
     
    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

