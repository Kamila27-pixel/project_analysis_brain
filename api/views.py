from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BrainScan
from .serializers import BrainScanSerializer

class BrainScanViewSet(viewsets.ModelViewSet):
    queryset = BrainScan.objects.all()
    serializer_class = BrainScanSerializer

from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

from rest_framework import viewsets
from .models import Patient, Doctor, BrainScan, ScanResult, Appointment, Report
from .serializers import PatientSerializer, DoctorSerializer, BrainScanSerializer, ScanResultSerializer, AppointmentSerializer, ReportSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class BrainScanViewSet(viewsets.ModelViewSet):
    queryset = BrainScan.objects.all()
    serializer_class = BrainScanSerializer

class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
