from django.shortcuts import render
from .models import Tarea
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

# Create your views here.

class TareaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tareas/registrar_tarea.html'
    model = Tarea
    login_url = 'users_app:user_login'
    success_url = reverse_lazy('tareas_app:listar_tareas')
    fields = [
        'fecha',
        'descripcion',
        'tipo',        
    ]

    def form_valid(self, form):
        tarea = form.save(commit=False)
        tarea.usuario = self.request.user        
        messages.success(self.request, 'Tarea registrada con éxito.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error("Ocurrió un error al procesar su solicitud, reintentar...")
        return response

class TareasListView(LoginRequiredMixin, ListView):
    template_name = 'tareas/listar_tareas.html'
    paginate_by = 10
    login_url = 'users_app:user_login'

    def get_queryset(self):
        tareas = Tarea.objects.all().order_by('-created')
        return tareas
