from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
import pandas as pd
import io

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
        tareas = Tarea.objects.all().order_by('-fecha')
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

        # Convertir los datos en un DataFrame
        data = {
            'Fecha': [tarea.fecha for tarea in tareas],
            'Tipo de tarea': [tarea.get_tipo_display() for tarea in tareas],
            'Descripción': [tarea.descripcion for tarea in tareas],            
            'Funcionario': [f"{tarea.usuario.nombre} {tarea.usuario.apellido}" for tarea in tareas],
        }
        df = pd.DataFrame(data)

        # Crear archivo Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Informe de Tareas')

        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="informe_tareas.xlsx"'
        return response
    return render(request, 'tareas/informe_de_tareas.html')

