from django.shortcuts import render
from .models import Lanzamiento
from .forms import CrearLanzamientoForm, LanzamientoUpdateForm
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
    paginate_by = 10
    context_object_name = 'lanzamientos'

    def get_queryset(self):
        lanzamientos = Lanzamiento.objects.all().order_by('estado', 'fecha')
        return lanzamientos

class LanzamientoUpdateEstado(LoginRequiredMixin, UpdateView):
    template_name = 'lanzamientos/actualizar_estado.html'
    model = Lanzamiento
    login_url = 'users_app:user_login'
    fields = ['estado',]
    success_url = reverse_lazy('lanzamientos_app:listado_lanzamientos')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = True
        self.object.save()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(LanzamientoUpdateEstado, self).form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Ocurrió un error al actualizar el estado, reintentar...")
        return response

class ActualizarLanzamiento(LoginRequiredMixin, UpdateView):
    model = Lanzamiento
    form_class = LanzamientoUpdateForm
    template_name = "lanzamientos/actualizar.html"
    success_url = reverse_lazy('lanzamientos_app:listado_lanzamientos')
    login_url = 'users_app:user_login'

    def form_valid(self, form):
        lanzamiento = form.save(commit=False)
        lanzamiento.usuario = self.request.user
        lanzamiento.save()
        messages.success(self.request, 'Lanzamiento actualizado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Ocurrió un error al actualizar el lanzamiento, reintentar...")
        return response