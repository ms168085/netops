from django.urls import path
from . import views

app_name = 'tareas_app'

urlpatterns = [
    path('registrar_tarea/', views.TareaCreateView.as_view(), name='registrar_tarea'),
    path('listar_tareas/', views.TareasListView.as_view(), name='listar_tareas'),
]