from django.db import models
from ..users.models import User

class Tarea(models.Model):
    usuario = models.ForeignKey(User, related_name="tarea_user", on_delete=models.CASCADE)
    descripcion = models.TextField("Descripción")
    fecha = models.DateField("Fecha")

    opciones = (
        ('0', 'Tarea Operativa'),
        ('1', 'Tarea Programada'),
        ('2', 'Falla/Disturbio')
    )
    tipo = models.CharField("Tipo de tarea", choices=opciones, max_length=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    def __str__(self):
        return str(self.id) + " )" +self.usuario.nombre + self.usuario.apellido + " - " + self.fecha