# -*- encoding: utf-8 -*-
from django.core.validators import RegexValidator

validador_numero_serie = RegexValidator(
                    r'^[A-Z]{3}-[0-9]{4}',
                    message='Debe ingresar un codigo valido ej: USM-1001',
                    code='Invalid Key')