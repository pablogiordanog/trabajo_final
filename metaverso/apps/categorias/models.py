from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    class Meta:
        ordering = ('nombre',) 

    def __str__(self) -> str:
        return self.nombre