from django.shortcuts import render

from rest_framework import viewsets

from encuestas.models import Encuesta, Vivienda, Pueblo
from encuestas.serializers import (EncuestaSerializer, ViviendaSerializer,
                                   PuebloSerializer)


# Create your views here.
# ViewSets define the view behavior.
class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer


class PuebloViewSet(viewsets.ModelViewSet):
    queryset = Pueblo.objects.all()
    serializer_class = PuebloSerializer
