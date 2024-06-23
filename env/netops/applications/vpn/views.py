from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView
from .forms import RegistrarVPNForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Vpn

# Create your views here.
class RegistrarVPN(LoginRequiredMixin, FormView):
    template_name = 'vpn/registrar.html'
    form_class = RegistrarVPNForm
    success_url = reverse_lazy('users_app:index')

    def form_valid(self, form):
        vpn = form.save(commit=False)
        vpn.usuario = self.request.user
        vpn.save()
        messages.success(self.request, 'La VPN ha sido creada con éxito.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la VPN. Por favor, revise los datos ingresados.')
        return self.render_to_response(self.get_context_data(form=form))

class ListVPN(LoginRequiredMixin, ListView):
    template_name = 'vpn/listado.html'
    paginate_by = 15
    model = Vpn
    context_object_name = 'vpns'
    ordering = ('apn_id')
