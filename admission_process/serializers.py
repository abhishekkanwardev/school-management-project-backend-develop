from .models import Class, AdmissionApplication, Appointment
from rest_framework import serializers
from django.utils import timezone
from django.forms.models import model_to_dict

class ClassSerializer(serializers.ModelSerializer):
    """
    Class that converts models to JSON
    """
    class Meta:
        model = Class
        fields = '__all__'


class AppointmentSerializers(serializers.ModelSerializer):
    # appointment_time = serializers.ChoiceField(source='get_appointment_time_display', choices=Appointment.TIMESLOT_LIST)
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
        

class AdmissionApplicationSerializer(serializers.ModelSerializer):
    appointment = serializers.SerializerMethodField()

    class Meta:
        model = AdmissionApplication
        exclude = ('is_active',)

    def get_appointment(self, object):
        associatedAppointment = Appointment.objects.filter(admission_application__id = object.id)
        if associatedAppointment:
            return model_to_dict(associatedAppointment.first())
        return None 


class AdmissionApplicationNonAuthSerializer(serializers.ModelSerializer):
    """
    Class that converts models to JSON
    """
    appointment = serializers.SerializerMethodField() 

    class Meta:
        model = AdmissionApplication
        exclude = ('is_active',)

    def get_appointment(self, object):
        associatedAppointment = Appointment.objects.filter(admission_application__id = object.id)
        if associatedAppointment:
            return model_to_dict(associatedAppointment.first())
        return None 
 

