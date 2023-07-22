from django import forms
from .models import Noticia

class FormNotice(forms.ModelForm):

    class Meta:
        model = Noticia
        fields=['titulo','autor','descripcion','published','imagen','categoria']
        
    