from rest_framework import serializers
from .models import Attendance, ClassAttendance
    
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


class ClassAttendanceSerializer(serializers.ModelSerializer):
    
    attendance_list = AttendanceSerializer(many=True, read_only=True) 

    class Meta:
        model = ClassAttendance
        fields = '__all__'
        read_only_fields = ['id']
