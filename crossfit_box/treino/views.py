from django.shortcuts import render
from rest_framework import viewsets
from treino.models import Training
from treino.serializers import TreinoSerializer


class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TreinoSerializer
