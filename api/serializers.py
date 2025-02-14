from rest_framework import serializers
from .models import CustomUser, Patient, Doctor, BrainScan, ScanResult, Appointment, Report, ResearchStudy, MedicalOrder, PatientHistory

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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

# Serializer dla lekarza
class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

# Serializer dla skanów mózgu
class BrainScanSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = BrainScan
        fields = '__all__'

# Serializer dla wyników skanów
class ScanResultSerializer(serializers.ModelSerializer):
    scan = BrainScanSerializer(read_only=True)

    class Meta:
        model = ScanResult
        fields = '__all__'

# Serializer dla wizyt lekarskich
class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

# Serializer dla raportów
class ReportSerializer(serializers.ModelSerializer):
    scan = BrainScanSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Report
        fields = '__all__'

# Serializer dla badań naukowych
class ResearchStudySerializer(serializers.ModelSerializer):
    researchers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ResearchStudy
        fields = '__all__'

# Serializer dla zleceń badań
class MedicalOrderSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = MedicalOrder
        fields = '__all__'

# Serializer dla historii pacjenta
class PatientHistorySerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientHistory
        fields = '__all__'

