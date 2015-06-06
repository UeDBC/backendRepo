from rest_framework import serializers
from encuestas.models import Encuesta, Vivienda, Pueblo


class EncuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encuesta


class ViviendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vivienda


class PuebloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pueblo
