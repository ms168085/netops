from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView

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
    context_object_name = 'tareas'

    def get_queryset(self):
        tareas = Tarea.objects.all().order_by('-created')
        return tareas

class InformeDeTareas(LoginRequiredMixin, TemplateView):
    template_name = 'tareas/informe_de_tareas.html'
    login_url = 'users_app:user_login'

# FUNCIÓN PARA DESCARGAR EL INFORME EN FORMATO EXCEL
def descargar_informe(request):
    if request.method == 'POST':
        fecha_desde = request.POST.get('fecha_desde')
        fecha_hasta = request.POST.get('fecha_hasta')
        tareas = Tarea.objects.filter(fecha__range=[fecha_desde, fecha_hasta])

        # Lógica para generar el informe
        # Por ejemplo, podrías generar un archivo CSV, PDF, etc.
        # Aquí simplemente devolvemos una respuesta de texto plano como ejemplo
        informe = "Informe de Tareas\n"
        for tarea in tareas:
            informe += f"{tarea.fecha} - {tarea.descripcion}\n"

        # Crear una respuesta HTTP con el contenido del informe
        response = HttpResponse(informe, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="informe_tareas.txt"'
        return response

    # Si el metodo no es POST
    return render(request, 'tareas_app/informe_de_tareas.html')