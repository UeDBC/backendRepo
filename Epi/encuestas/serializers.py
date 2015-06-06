from rest_framework import serializers
from encuestas.models import (Encuesta, Vivienda, Pueblo, Individuo, Patologia)


class EncuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encuesta


class PuebloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pueblo


class ViviendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vivienda


class IndividuoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individuo


class PatologiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patologia
