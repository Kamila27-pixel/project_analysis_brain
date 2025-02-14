from rest_framework import serializers
from .models import CustomUser, Patient, Doctor, BrainScan, ScanResult, Appointment, Report

# Serializer dla użytkownika
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'date_joined', 'account_status']

# Serializer dla rejestracji użytkownika
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

# Serializer dla pacjenta
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

# Serializer dla lekarza
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

# Serializer dla skanów mózgu
class BrainScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrainScan
        fields = '__all__'

# Serializer dla wyników skanów
class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = '__all__'

# Serializer dla wizyt lekarskich
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

# Serializer dla raportów
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

