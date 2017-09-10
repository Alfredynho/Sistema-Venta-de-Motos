# -*- encoding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

class MessengerInfo(models.Model):

    messenger_id = models.CharField(
        verbose_name=_('Messenger ID'),
        max_length=255,
        blank=True,
        null=True
    )

    nombre = models.CharField(
        verbose_name=_('Nombre'),
        max_length=150,
        blank=True,
        null=True,        
    )

    apellido = models.CharField(
        verbose_name=_('Apellido'),
        max_length=150,
        blank=True,
        null=True,
    )

    foto_perfil = models.CharField(
        verbose_name=_('Foto de Perfil'),
        max_length=150,
        blank=True,
        null=True,        
    )

    lugar = models.CharField(
        verbose_name=_('Lugar'),
        max_length=150,
        blank=True,
        null=True,        
    )

    zona_horaria = models.CharField(
        verbose_name=_('Zona Horaria'),
        max_length=150,
        blank=True,
        null=True,        
    )

    genero = models.CharField(
        verbose_name=_('Género'),
        max_length=150,
        blank=True,
        null=True,        
    )

    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name=_('Usuario')
        verbose_name_plural=_('Usuarios')



