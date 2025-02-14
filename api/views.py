from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.utils.timezone import now
from .models import (
    CustomUser, Patient, Doctor, BrainScan, ScanResult, Appointment, Report, 
    ResearchStudy, MedicalOrder, PatientHistory
)
from .serializers import (
    UserSerializer, RegisterSerializer, PatientSerializer, DoctorSerializer,
    BrainScanSerializer, ScanResultSerializer, AppointmentSerializer, 
    ReportSerializer, ResearchStudySerializer, MedicalOrderSerializer, PatientHistorySerializer
)

# Paginacja dla API
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Rejestracja użytkownika (opcjonalne)
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# CRUD: Użytkownicy
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Tylko admini mogą zarządzać użytkownikami
    pagination_class = StandardResultsSetPagination

# CRUD: Pacjenci
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Lekarze
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Skan mózgu + filtr + niestandardowy endpoint
class BrainScanViewSet(viewsets.ModelViewSet):
    serializer_class = BrainScanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = BrainScan.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    # Niestandardowy endpoint: Lista skanów dla konkretnego pacjenta
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>\d+)')
    def patient_scans(self, request, patient_id=None):
        scans = BrainScan.objects.filter(patient__id=patient_id)
        serializer = self.get_serializer(scans, many=True)
        return Response(serializer.data)

# CRUD: Wyniki skanów
class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Wizyty lekarskie + niestandardowy endpoint
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = StandardResultsSetPagination

    # Niestandardowy endpoint: Zestawienie miesięczne wizyt
    @action(detail=False, methods=['get'], url_path='monthly-summary')
    def monthly_summary(self, request):
        current_month = now().month
        appointments = Appointment.objects.filter(date__month=current_month).values('date__month').annotate(count=Count('id'))
        return Response(appointments)

# CRUD: Raporty medyczne
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Badania naukowe
class ResearchStudyViewSet(viewsets.ModelViewSet):
    queryset = ResearchStudy.objects.all()
    serializer_class = ResearchStudySerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Zlecenia badań
class MedicalOrderViewSet(viewsets.ModelViewSet):
    queryset = MedicalOrder.objects.all()
    serializer_class = MedicalOrderSerializer
    pagination_class = StandardResultsSetPagination

# CRUD: Historia pacjentów
class PatientHistoryViewSet(viewsets.ModelViewSet):
    queryset = PatientHistory.objects.all()
    serializer_class = PatientHistorySerializer
    pagination_class = StandardResultsSetPagination

