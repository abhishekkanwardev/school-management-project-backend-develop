from rest_framework import serializers
from .models import Attendance
    
from datetime import date
    
class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']


    def validate_date(self, datevalue):  
        today = date.today()
        if datevalue > today:
            raise serializers.ValidationError("The date of attendance cannot be a future date.!")
        return datevalue
