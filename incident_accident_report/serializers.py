from .models import IncidentAccidentReport
from rest_framework import serializers
from accounts.serializers import StudentDetailForContainsStudentsSerializer



class IncidentAccidentReportSErializer(serializers.ModelSerializer):
    student = StudentDetailForContainsStudentsSerializer(read_only=True) 

    class Meta:
        model = IncidentAccidentReport
        fields = "__all__"
        
