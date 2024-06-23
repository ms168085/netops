from django.urls import path
from . import views

app_name = 'vpn_app'

urlpatterns = [
    path('registrar_vpn/', views.RegistrarVPN.as_view(), name="registrar_vpn"),
    path('lista_vpns/', views.ListVPN.as_view(), name="lista_vpns"),
    path('buscar/<apnid>/', views.buscar_por_APNID, name="buscar_por_apnid"),
    path('buscarAPN/<texto>/', views.buscar_por_APN, name="buscar_por_apn"),
    path('actualizar/<int:pk>/', views.UpdateVPN.as_view(), name='actualizar_vpn'),
]

