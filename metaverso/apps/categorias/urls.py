from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import ListCategory, AddCategory, UpdateCategory, DeleteCategory

app_name = 'apps.categorias'

urlpatterns = [
    path('list/', ListCategory.as_view(), name='list'),
    path("add_category/", AddCategory.as_view(), name='add_category'),
    path("update_category/<int:pk>",
         UpdateCategory.as_view(), name='update_category'),
    path("delete_category/<int:pk>", DeleteCategory.as_view(), name='delete_category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
