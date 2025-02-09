from rest_framework import serializers
from .models import BrainScan

class BrainScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrainScan
        fields = '__all__'
