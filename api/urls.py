from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, RegisterView, PatientViewSet, DoctorViewSet, BrainScanViewSet, 
    ScanResultViewSet, AppointmentViewSet, ReportViewSet, ResearchStudyViewSet, 
    MedicalOrderViewSet, PatientHistoryViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'patients', PatientViewSet, basename="patients")
router.register(r'doctors', DoctorViewSet, basename="doctors")
router.register(r'scans', BrainScanViewSet, basename="scans")  # ✅ Naprawione!
router.register(r'scan-results', ScanResultViewSet, basename="scan-results")
router.register(r'appointments', AppointmentViewSet, basename="appointments")
router.register(r'reports', ReportViewSet, basename="reports")
router.register(r'research-studies', ResearchStudyViewSet, basename="research-studies")
router.register(r'medical-orders', MedicalOrderViewSet, basename="medical-orders")
router.register(r'patient-history', PatientHistoryViewSet, basename="patient-history")

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]

