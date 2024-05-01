from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# PermissionsMixin nos permite crear superusuarios desde la consola

# Modelo de usuario
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # Defino cual sera el campo para hacer login, "usuario"
    USERNAME_FIELD = 'email'

    # Usando Manager
    objects = UserManager()

    def get_full_name(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
