from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Machine, Section, Step, StepBlock, Tag
from .serializers import MachineSerializer, SectionSerializer, StepSerializer, StepBlockSerializer, TagSerializer, MachineBasicSerializer,  TagSerializer, TagWithMachinesSerializer
from .permissions import ReadOnlyOrAdmin
from .filters import MachineFilter
from django.shortcuts import render
from .models import Machine
from django.conf import settings
import requests
from django.shortcuts import get_object_or_404

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['difficulty', 'tags__name', 'platform']  # filtros planos
    search_fields = ['name', 'summary']
    ordering_fields = ['created_at', 'name']
    lookup_field = 'slug'

class MachineBasicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineBasicSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['difficulty', 'tags__name', 'platform']  
    filterset_class = MachineFilter
    search_fields = ['name', 'summary']  
    ordering_fields = ['created_at', 'name']

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

def machine_detail(request, machine_id):
    machine = get_object_or_404(Machine, slug=machine_id)
    return render(request, "machine_detail.html", {"machine": machine})

"""
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['machine']

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['section']

class StepBlockViewSet(viewsets.ModelViewSet):
    queryset = StepBlock.objects.all()
    serializer_class = StepBlockSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['step', 'type']

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
"""
