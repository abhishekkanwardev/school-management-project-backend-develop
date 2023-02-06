from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Class, AdmissionApplication
from .serializers import ClassSerializer, AdmissionApplicationSerializer, AppointmentSerializers
from rest_framework.permissions import AllowAny
from .permission import IsAdminUser
from .models import Appointment

class ClassViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    

class AdmissionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = AdmissionApplication.objects.all()
    serializer_class = AdmissionApplicationSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAdminUser, ]
        return super(AdmissionViewSet, self).get_permissions()


class AppointmentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    
    def get_serializer_context(self):
        return {"request": self.request}
