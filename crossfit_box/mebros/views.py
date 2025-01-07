from django.shortcuts import render
from rest_framework import viewsets
from mebros.models import Member
from mebros.serializers import MenbroSerializer


class MembroViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MenbroSerializer
