from django import forms

from .models import Reclamo


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Reclamo
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')
    
