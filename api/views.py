from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BrainScan
from .serializers import BrainScanSerializer

class BrainScanViewSet(viewsets.ModelViewSet):
    queryset = BrainScan.objects.all()
    serializer_class = BrainScanSerializer
