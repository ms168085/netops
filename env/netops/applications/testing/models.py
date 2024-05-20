from django.db import models
from ..users.models import User


class Testing(models.Model):
    funcionalidad = models.CharField("Funcionalidad", max_length=200)
    comentario = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, related_name="tareas", on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Testing"
        verbose_name_plural = "Testings"
    
    def __str__(self):
        return self.funcionalidad
