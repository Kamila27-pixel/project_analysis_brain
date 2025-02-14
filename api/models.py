from django.contrib.auth.models import AbstractUser
from django.db import models

# Model użytkownika (rozszerzony)
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    date_joined = models.DateTimeField(auto_now_add=True)
    account_status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


# Model pacjenta
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.age} lat"


# Model lekarza
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr {self.user.username} - {self.specialization}"


# Model skanów mózgu
class BrainScan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='brain_scans/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    analysis_result = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Skan {self.id} - {self.patient.user.username}"


# Model wyników analizy skanów
class ScanResult(models.Model):
    scan = models.OneToOneField(BrainScan, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255)
    probability = models.FloatField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Wynik dla skanu {self.scan.id} - {self.diagnosis}"


# Model wizyt lekarskich
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Wizyta: {self.patient.user.username} u {self.doctor.user.username} - {self.date.strftime('%Y-%m-%d %H:%M')}"


# Model raportów medycznych
class Report(models.Model):
    scan = models.ForeignKey(BrainScan, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f"Raport dla skanu {self.scan.id} - {self.doctor.user.username}"

