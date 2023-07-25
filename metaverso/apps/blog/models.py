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
    
    





   

