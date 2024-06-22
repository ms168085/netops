from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegistrarVPNForm

# Create your views here.
class RegistrarVPN(FormView):
    template_name = 'vpn/registrar.html'
    form_class = RegistrarVPNForm
    success_url = '/'
