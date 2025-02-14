from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrainScanViewSet

router = DefaultRouter()
router.register(r'scans', BrainScanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, BrainScanViewSet, ScanResultViewSet, AppointmentViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'scans', BrainScanViewSet)
router.register(r'scan_results', ScanResultViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns += router.urls
