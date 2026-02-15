from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Family, Task
from .serializers import TareaSerializer, FamiliaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TareaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'family']


class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = FamiliaSerializer
