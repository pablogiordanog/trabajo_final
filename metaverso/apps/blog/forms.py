from django import forms
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuarios
        fields = ['first_name','last_name','username','fecha_nacimiento', 'email', 'password1', 'password2', 'imagen']
       

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        
        
        
    
   