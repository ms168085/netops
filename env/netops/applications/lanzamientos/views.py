from django.shortcuts import render
from .models import Lanzamiento
from .forms import CrearLanzamientoForm
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CrearLanzamiento(LoginRequiredMixin, CreateView):
    template_name = "lanzamientos/crear.html"
    model = Lanzamiento
    form_class = CrearLanzamientoForm
    login_url = 'users_app:user_login'
    success_url = reverse_lazy('lanzamientos_app:listado_lanzamientos')

    def form_valid(self, form):
        lanzamiento = form.save(commit=False)
        lanzamiento.usuario = self.request.user  # Asignar el usuario logueado
        lanzamiento.estado = False
        lanzamiento.save()
        messages.success(self.request, 'Lanzamiento registrado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form errors:", form.errors)
        response = super().form_invalid(form)
        messages.error(self.request, "Ocurrió un error al procesar el lanzamiento, reintentar...")
        return response


class ListadoLanzamientos(LoginRequiredMixin, ListView):
    template_name = "lanzamientos/listado.html"

    def get_queryset(self):
        lanzamientos = Lanzamiento.objects.all().order_by('estado', 'fecha')
        return lanzamientos
