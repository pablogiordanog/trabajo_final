from django.db import models
from django.utils import timezone

from apps.categorias.models import Categoria

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=20, null=False)
    descripcion = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias', default='noticias/notice_default.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-published',)    