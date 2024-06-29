from django import forms
from .models import Lanzamiento

class CrearLanzamientoForm(forms.ModelForm):
    class Meta:
        model = Lanzamiento
        exclude = ['usuario']