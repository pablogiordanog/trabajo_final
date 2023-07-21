from django.contrib import admin
from .models import Noticias
from .models import Usuarios

admin.site.register(Noticias)
admin.site.register(Usuarios)
