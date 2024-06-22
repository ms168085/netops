from django import forms
from .models import Vpn

class RegistrarVPNForm(forms.ModelForm):
    class Meta:
        model = Vpn
        fields = "__all__"