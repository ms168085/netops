from django.db import models
from ..users.models import User

# Create your models here.
class Vpn(models.Model):
    #Usuario que registra la VPN
    usuario = models.ForeignKey(User, related_name="vpn_user", on_delete=models.CASCADE)

    con_sitio_central = models.BooleanField("Con sitio central")
    vpn_instance = models.CharField("VPN instance", max_length=20)

    #Armado del BGP
    tinco_movil = models.CharField("Tinco movil", max_length=10)
    route_distinguisher = models.CharField("Route distinguisher", max_length=8)
    vprn_id = models.CharField("VPRN Id", max_length=8)
    ip_mag = models.CharField("IP de MAG", max_length=15)
    peer_mag = models.CharField("Peer de MAG", max_length=15)
    ip_mun = models.CharField("IP de MUN", max_length=15)
    peer_mun = models.CharField("Peer de MUN", max_length=15)    

    #Conectividad de moviles
    CONECTIVIDAD_MOVILES = (
        ("1", "Full mesh"),
        ("2", "Hub & spoke"),
    )
    conectividad_entre_moviles = models.CharField("Conectividad entre moviles", max_length=1, choices=CONECTIVIDAD_MOVILES)

    #Armado ACL
    nombre_pool = models.CharField("Nombre del pool", max_length=15)
    server_ip = models.CharField("Server IP", max_length=15)
    wildcard = models.CharField("Wildcard", max_length=15)
    acl_node = models.CharField("ACL Node", max_length=15)
    nombre_acl = models.CharField("Nombre ACL", max_length=30)
    prioridad = models.IntegerField("Prioridad")    

    #Armado pool de moviles
    TIPO_DE_IP = (
        ("1", "Fijas"),
        ("2", "Dinamicas"),
    )
    nombre_pool_moviles = models.CharField("Nombre del pool moviles", max_length=15)
    tipo_ip = models.CharField("Tipo de IPs", max_length=1, choices=TIPO_DE_IP)
    primer_ip_mag = models.CharField("Primer IP MAG", max_length=15)
    ultima_ip_mag = models.CharField("Última IP MAG", max_length=15)
    primer_ip_mun = models.CharField("Primer IP MUN", max_length=15)
    ultima_ip_mun = models.CharField("Última IP MUN", max_length=15)
    roaming = models.BooleanField()
    apn = models.CharField("APN", max_length=15)
    dns_1 = models.CharField("DNS 1", max_length=15)
    dns_2 = models.CharField("DNS 2", max_length=15)

    cliente_acm = models.CharField("Cliente ACM", max_length=15)
    apn_id = models.IntegerField("APN ID", unique=True)
    tinco_fija = models.CharField("TINCO fija", max_length=15)

    #Datos del cliente/empresa
    empresa = models.CharField("Empresa", max_length=100)
    ip_router = models.CharField("IP Router", max_length=15)
    contacto = models.CharField("Contacto", max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "VPN"
        verbose_name_plural = "VPNs"
        ordering = ["-created"]

    def __str__(self):
        return f'APN: {self.apn} - APN ID: {self.apn_id}'