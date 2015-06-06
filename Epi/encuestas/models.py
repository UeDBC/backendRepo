# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Encuesta(models.Model):
    """docstring for Encuesta"""
    encuesta = models.CharField(verbose_name='ID Encuesta', max_length=256)
    fecha = models.DateField()
    vivienda = models.OneToOneField('Vivienda')


class Vivienda(models.Model):
    OP_AGUA = (
        ('Agua de red', 'red'),
        ('Agua de Pozo', 'pozo'),
        ('Otra fuente de agua', 'otra')
    )
    """docstring for Vivienda"""

    pueblo = models.ForeignKey('Pueblo')
    calle = models.CharField(max_length=256)
    numero = models.IntegerField()
    manzana = models.CharField(max_length=256)
    lote = models.IntegerField()
    # fuente de contaminacion
    # latitud
    # longitud
    agua = models.BooleanField(verbose_name='Tiene agua de red?', choices=OP_AGUA)
    pavimento = models.BooleanField(verbose_name='Calle Pavimentada')
    # tapa_tanque = models.BooleanField(label='Los tanques de agua tienen tapa?')
    # limpieza_tanque = models.BooleanField(label='Ha realizado limpieza de tanque de agua durante el último año?')
    num_fallecidos = models.IntegerField(default=0)


class Individuo(models.Model):
    """docstring for Individuo"""
    OP_SEXO = (
        ('Masculino', 'masculino'),
        ('Femenino', 'femenino'),
        ('Otro', 'otro')
    )

    individuo = models.CharField(verbose_name='ID Individuo', max_length=256)
    nombres = models.CharField(max_length=256)
    # apellidos = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=256, choices=OP_SEXO)
    tiempo_residencia = models.IntegerField(default=0)
    problema_salud = models.BooleanField(verbose_name='Problemas de salud en los ultimos 20 años')
    # patologias = models.ManyToManyField('ProblemaSalud', verbose_name='Patologías')
    # estado_de_salud / patologias
    # nivel_educativo
    # ocupacion
    # actividades_de_riesgo
    # tiempo en localidad =
    vivienda = models.ForeignKey('Vivienda', blank=False, null=False)


class Pueblo(models.Model):
    """docstring for Pueblo"""

    nombres = models.CharField(max_length=256)
    # factores_de_contaminacion = models.ManyToManyField('FactoresContaminacion')


# class PercepcionRiesgoAmbiental(object):
#     """docstring for PercepcionRiesgoAmbiental"""

#     usa_agrotoxico
#     lavado_junto_flia
#     fumigaciones
#     pasa_mosquito
#     pasa_avioneta
#     guarda_agrotoxico
#     guarda_envases
#     reutiliza_envases
#     recibio_informacion
#     danios_plantas
#     danios_animales
#     ninios_expuestos



#     def __init__(self, arg):
#         super(PercepcionRiesgoAmbiental, self).__init__()
#         self.arg = arg



# Vivienda

# Patologia


# Embarazo

# class FuenteContaminacion(object):
#     """docstring for FuenteContaminacion"""
#     def __init__(self, arg):
#         super(FuenteContaminacion, self).__init__()
#         self.arg = arg


# ActividadesRiesgo

# EstadoSalud