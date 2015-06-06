# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Encuesta(models.Model):
    """docstring for Encuesta"""
    identificador = models.CharField(verbose_name='ID Encuesta', max_length=256)
    fecha = models.DateField()
    vivienda = models.OneToOneField('Vivienda', null=True, blank=True)

    def __unicode__(self):
        return u'Encuesta %s' % self.identificador


class Vivienda(models.Model):
    """docstring for Vivienda"""
    OP_AGUA = (
        ('Agua de red', 'red'),
        ('Agua de Pozo', 'pozo'),
        ('Otra fuente de agua', 'otra')
    )

    pueblo = models.ForeignKey('Pueblo', null=True, blank=True)
    calle = models.CharField(max_length=256, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    manzana = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    # fuente de contaminacion
    # latitud
    # longitud
    agua = models.CharField(max_length=256, verbose_name='Tiene agua de red?',
                            choices=OP_AGUA)
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
    patologias = models.ManyToManyField('Patologia', verbose_name='Patologías')
    # estado_de_salud / patologias
    # nivel_educativo
    # ocupacion
    # actividades_de_riesgo
    # tiempo en localidad =
    vivienda = models.ForeignKey('Vivienda', blank=False, null=False)

    def __unicode__(self):
        return self.nombres


class Pueblo(models.Model):
    """docstring for Pueblo"""
    nombre = models.CharField(max_length=256)
    # factores_de_contaminacion = models.ManyToManyField('FactoresContaminacion')

    def __unicode__(self):
        return self.nombre


class Patologia(models.Model):
    identificador = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)

    def __unicode__(self):
        return self.nombre


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


# Embarazo

# class FuenteContaminacion(object):
#     """docstring for FuenteContaminacion"""
#     def __init__(self, arg):
#         super(FuenteContaminacion, self).__init__()
#         self.arg = arg


# ActividadesRiesgo

# EstadoSalud