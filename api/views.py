from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import CustomUser, Patient, Doctor, BrainScan, ScanResult, Appointment, Report, ResearchStudy, MedicalOrder, PatientHistory
from .serializers import (
    UserSerializer, RegisterSerializer, PatientSerializer, DoctorSerializer,
    BrainScanSerializer, ScanResultSerializer, AppointmentSerializer, 
    ReportSerializer, ResearchStudySerializer, MedicalOrderSerializer, PatientHistorySerializer
)

# Klasa paginacji dla API
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Rejestracja użytkownika
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Każdy może się zarejestrować

# Widok użytkowników
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

# Widok pacjentów
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = StandardResultsSetPagination

# Widok lekarzy
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = StandardResultsSetPagination

# Widok skanów mózgu z filtrowaniem po statusie
class BrainScanViewSet(viewsets.ModelViewSet):
    serializer_class = BrainScanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = BrainScan.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

# Widok wyników skanów
class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer
    pagination_class = StandardResultsSetPagination

# Widok wizyt lekarskich
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = StandardResultsSetPagination

# Widok raportów
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = StandardResultsSetPagination

# Widok badań naukowych (Research Studies)
class ResearchStudyViewSet(viewsets.ModelViewSet):
    queryset = ResearchStudy.objects.all()
    serializer_class = ResearchStudySerializer
    pagination_class = StandardResultsSetPagination

# Widok zleceń badań (Medical Orders)
class MedicalOrderViewSet(viewsets.ModelViewSet):
    queryset = MedicalOrder.objects.all()
    serializer_class = MedicalOrderSerializer
    pagination_class = StandardResultsSetPagination

# Widok historii pacjentów
class PatientHistoryViewSet(viewsets.ModelViewSet):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer
    pagination_class = StandardResultsSetPagination
