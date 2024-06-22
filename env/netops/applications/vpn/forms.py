from django import forms
from .models import Vpn

class RegistrarVPNForm(forms.ModelForm):
    class Meta:
        model = Vpn
        fields = fields = [
            'con_sitio_central',
            'vpn_instance',
            'tinco_movil',
            'route_distinguisher',
            'vprn_id',
            'ip_mag',
            'peer_mag',
            'ip_mun',
            'peer_mun',
            'conectividad_entre_moviles',
            'nombre_pool',
            'server_ip',
            'wildcard',
            'acl_node',
            'nombre_acl',
            'prioridad',
            'nombre_pool_moviles',
            'primer_ip_mag',
            'ultima_ip_mag',
            'primer_ip_mun',
            'ultima_ip_mun',
            'roaming',
            'apn',
            'dns_1',
            'dns_2',
            'cliente_acm',
            'apn_id',
            'tinco_fija',
            'empresa',
            'ip_router',
            'contacto'
        ]