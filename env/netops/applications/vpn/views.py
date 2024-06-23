from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, UpdateView
from .forms import RegistrarVPNForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Vpn
from django.contrib.auth.decorators import login_required

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

class UpdateVPN(LoginRequiredMixin, UpdateView):
    model = Vpn
    template_name = 'vpn/actualizar.html'
    form_class = RegistrarVPNForm
    success_url = reverse_lazy('vpn_app:lista_vpns')

    def form_valid(self, form):
        vpn = form.save(commit=False)
        vpn.usuario = self.request.user  #Asignar el usuario logueado
        vpn.save()
        messages.success(self.request, 'La VPN ha sido actualizada con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar la VPN. Por favor, revise los datos ingresados.')
        return self.render_to_response(self.get_context_data(form=form))

@login_required
def buscar_por_APNID(request, apnid):
    try:
        vpn = get_object_or_404(Vpn, apn_id=apnid)
        data = {
            'vpn': vpn
        }
        return render(request, 'vpn/buscar.html', data)
    except Vpn.DoesNotExist:
        messages.error(request, "No existe VPN con ese APN ID")
        return redirect('users_app:index')
    except Exception as e:
        messages.error(request, "No se encontró VPN para ese APN ID")
        return redirect('users_app:index')

@login_required
def buscar_por_APN(request, texto):
    try:
        vpn = get_object_or_404(Vpn, apn__iexact=texto)
        data = {
            'vpn':vpn
        }
        return render(request, 'vpn/buscar.html', data)
    except Vpn.DoesNotExist:
        messages.error(request, "No existe VPN con ese APN")
        return redirect('users_app:index')
    except Exception as e:
        messages.error(request, "No se encontró VPN para ese APN")
        return redirect('users_app:index')