from .models import IncidentAccidentReport
from rest_framework import serializers



class IncidentAccidentReportSErializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentAccidentReport
        fields = "__all__"
        
