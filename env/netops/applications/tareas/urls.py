from django.urls import path
from . import views

app_name = 'tareas_app'

urlpatterns = [
    path('registrar_tarea/', views.TareaCreateView.as_view(), name='registrar_tarea'),
    path('listar_tareas/', views.TareasListView.as_view(), name='listar_tareas'),
    path('informe_de_tareas/', views.InformeDeTareas.as_view(), name='informe_de_tareas'),
    path('descargar_informe/', views.descargar_informe, name='descargar_informe'),
]