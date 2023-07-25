from django.db import models
from django.utils import timezone



# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    class Meta:
        ordering = ('nombre',) 

    def __str__(self) -> str:
        return self.nombre
    
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=100)  
    contenido = models.TextField() 
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias', default='noticias/notice_default.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-published',)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=20)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentario {self.id} de {self.autor} en {self.noticia.titulo}'
        
