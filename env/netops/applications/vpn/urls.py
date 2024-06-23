from django.urls import path
from . import views

app_name = 'vpn_app'

urlpatterns = [
    path('registrar_vpn/', views.RegistrarVPN.as_view(), name="registrar_vpn"),
    path('lista_vpns/', views.ListVPN.as_view(), name="lista_vpns"),
]

