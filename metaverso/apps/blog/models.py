from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):  #MODELO USUARIOS
    username = models.CharField(max_length=150, unique=True)
    password=models.CharField(max_length=150, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_colaborador = models.BooleanField('es_colaborador', default=False)
    imagen = models.ImageField(
        null=True, blank=True, upload_to='usuarios', default='usuarios/user.png')
    email = models.EmailField(null=True, blank=True)
    
    USERNAME_FIELD= 'username'

    def __str__(self):
        return self.username
    



class Noticias(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to='blog', default='blog/img.jpg')
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    
    def __srt__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-fecha_publicacion',)
    
    
    class Categorias(models.Model):
     nombre = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nombre
    
    





   

