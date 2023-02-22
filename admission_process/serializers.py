from .models import Class, AdmissionApplication, Appointment
from rest_framework import serializers
from django.utils import timezone

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
        

class AppointmentSerializers(serializers.ModelSerializer):
    appointment_time = serializers.ChoiceField(source='get_appointment_time_display', choices=Appointment.TIMESLOT_LIST)
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ['status']
        
    def validate_appointment_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the past")
        return value
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']
        role = request.user.groups.all().values_list('name', flat=True)
        if 'admin' in role or 'teacher' in role:
            fields["status"].read_only = False
        else:
            fields["status"].read_only = True
        return fields
    
class AppointmentUpdateStatusByIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ['id']