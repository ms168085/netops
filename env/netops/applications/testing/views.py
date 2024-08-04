from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Testing
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoTesting(LoginRequiredMixin, ListView):
    template_name = "testing/listado.html"
    paginate_by = 12
    model = Testing
    context_object_name = 'funcionalidades'
    ordering = ('created')

class ActualizarTesting(LoginRequiredMixin, UpdateView):
    template_name = "testing/actualizar.html"
    model = Testing    
    fields = [
        "comentario",
    ]
    success_url = reverse_lazy("testing_app:listado_testing")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Obtengo el usuario que actualmente autenticado en el campo 'usuario'
        self.object.usuario = self.request.user
        # Actualizo el campo 'comentario' con los datos del formulario
        self.object.comentario = request.POST.get('comentario')
        # Guardo los cambios en la base de datos
        self.object.save()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(ActualizarTesting, self).form_valid(form)
    
