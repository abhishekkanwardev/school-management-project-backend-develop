from .models import Class, AdmissionApplication
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    """
    Class that converts models to JSON
    """
    class Meta:
        model = Class
        fields = '__all__'
        
        
class AdmissionApplicationSerializer(serializers.ModelSerializer):
    """
    Class that converts models to JSON
    """
    class Meta:
        model = AdmissionApplication
        exclude = ('is_active',)