from django.shortcuts import render
from rest_framework import viewsets
from planotreino.models import WorkoutPlan
from planotreino.serializer import PlanoSerializer


class PlanoTreinoViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = PlanoSerializer
