from django.db import models

class Lanzamiento(models.Model):
    operadora = models.CharField("Operadora", max_length=100)
    pais = models.CharField("País", max_length=40)
    descripcion = models.TextField("Descripción")
    fecha = models.DateField("Fecha")
    estado = models.BooleanField(default=False)

    mcc = models.CharField("MCC", max_length=3)
    mnc = models.CharField("MNC", max_length=3)
    nc = models.CharField("NC", max_length=3)
    cc = models.CharField("NC", max_length=3)

    dmrt = models.CharField("DMRT", max_length=4)

    CARRIERS = (
        ("1", "Syniverse"),
        ("2", "Comfone"),
    )
    carrier = models.CharField("Carrier", max_length=1, choices=CARRIERS)

    ir21 = models.ImageField(upload_to='lanzamientos', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lanzamiento"
        verbose_name_plural = "Lanzamientos"

    def __str__(self):
        return f'{self.operadora} - Fecha: {self.fecha}'
