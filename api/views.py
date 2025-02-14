from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import CustomUser, Patient, Doctor, BrainScan, ScanResult, Appointment, Report
from .serializers import (
    UserSerializer, RegisterSerializer, PatientSerializer, DoctorSerializer,
    BrainScanSerializer, ScanResultSerializer, AppointmentSerializer, ReportSerializer
)

# Rejestracja użytkownika
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

# Widok użytkowników
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Widok pacjentów
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Widok lekarzy
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Widok skanów mózgu
class BrainScanViewSet(viewsets.ModelViewSet):
    queryset = BrainScan.objects.all()
    serializer_class = BrainScanSerializer

# Widok wyników skanów
class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer

# Widok wizyt lekarskich
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Widok raportów
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

