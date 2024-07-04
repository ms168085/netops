from django.urls import path
from . import views

app_name = 'lanzamientos_app'

urlpatterns = [
    path('crear_lanzamiento/', views.CrearLanzamiento.as_view(), name="crear_lanzamiento"),
    path('listado_lanzamientos/', views.ListadoLanzamientos.as_view(), name="listado_lanzamientos"),
    path('actualizar_estado/<pk>/', views.LanzamientoUpdateEstado.as_view(), name="actualizar_estado"),
    path('lanzamientos/actualizar/<int:pk>/', views.ActualizarLanzamiento.as_view(), name='actualizar_lanzamiento'),
    # SCRIPTS
    path('lanzamiento_hss_mag/<int:id>/', views.hss_mag, name='lanzamiento_hss_mag'), # HSS MAG
    path('lanzamiento_hss_mun/<int:id>/', views.hss_mun, name='lanzamiento_hss_mun'), # HSS MUN
]
