from django.shortcuts import render

from rest_framework import viewsets, views, authentication, permissions

from encuestas.models import Encuesta, Vivienda, Pueblo, Individuo, Patologia

from encuestas.serializers import (EncuestaSerializer, ViviendaSerializer,
                                   PuebloSerializer, IndividuoSerializer,
                                   PatologiaSerializer)


from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


class IndividuoViewSet(viewsets.ModelViewSet):
    queryset = Individuo.objects.all()
    serializer_class = IndividuoSerializer


class PatologiaViewSet(viewsets.ModelViewSet):
    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer


class EncuestaJSON(views.APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)


    def post(self, request, format=None):
        #RECIBE EL JSON DE LA ENCUESTA COMPLETA
        print request.data

