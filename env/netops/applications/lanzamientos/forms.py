from django import forms
from .models import Lanzamiento

class CrearLanzamientoForm(forms.ModelForm):
    class Meta:
        model = Lanzamiento
        exclude = ['usuario']

class LanzamientoUpdateForm(forms.ModelForm):
    class Meta:
        model = Lanzamiento
        # Se excluye el campo usuario porque lo toma automaticamente de quien este logueado
        exclude = ['usuario']