from django import forms
from .models import Noticia

class FormNotice(forms.ModelForm):

    class Meta:
        model = Noticia
        fields=['titulo','autor','descripcion','published','imagen','categoria']
        
        
        
class AddNoticeForm(forms.ModelForm):
    contenido = forms.CharField(widget=forms.Textarea) 

    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'categoria']
        
    