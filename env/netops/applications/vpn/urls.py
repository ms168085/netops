from django.urls import path
from . import views

app_name = 'vpn_app'

urlpatterns = [
    path('registrar_vpn/', views.RegistrarVPN.as_view(), name="registrar_vpn"),
]

"""
urlpatterns = [
    path('listado_testing/', views.ListadoTesting.as_view(), name="listado_testing"),
    path('actualizar_testing/<pk>/', views.ActualizarTesting.as_view(), name="actualizar_testing"),    
]
"""