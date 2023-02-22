from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Class, AdmissionApplication
from .serializers import ClassSerializer, AdmissionApplicationSerializer, AppointmentSerializers, AppointmentUpdateStatusByIdSerializers
from rest_framework.permissions import AllowAny
from .permission import IsAdminUser
from .models import Appointment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from copy import copy

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
            self.permission_classes = [AllowAny, ]
        return super(AdmissionViewSet, self).get_permissions()


class AppointmentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

    def get_serializer_context(self):
        return {"request": self.request}


class AppointmentTimeAvailableStateList(APIView):

    def get(self, request):
        distincDatesQuery = Appointment.objects.order_by('appointment_date').values('appointment_date').distinct()
        timeslots = Appointment.TIMESLOT_LIST
        dateWithTimeSlots = list()

        for appObject in distincDatesQuery:
            appDate = appObject['appointment_date']
            timeAvailableList = list()

            for timeslot in timeslots:
                isExistData = Appointment.objects.filter(appointment_date=appDate, appointment_time = timeslot[0], status = 'Accept').exists()
                timeAvailableList.append({'id':timeslot[0], 'value': timeslot[1], 'is-available': not isExistData})
            dateWithTimeSlots.append({'date':appDate, 'timeslot-list': timeAvailableList})

        return Response(dateWithTimeSlots)
    

class AppointmentUpdateStatusById(APIView):

    def get_object(self,pk):
        appointment_instance = get_object_or_404(Appointment, pk=pk)
        return appointment_instance
        
    def put(self, request, pk):

        appointmentToUpdate = self.get_object(pk = pk)
        newAppointment = copy(appointmentToUpdate)
        appStatus = request.data['status']
        newAppointment.status = appStatus

        if appStatus == 'Reject':
            newAppointment.reject_message = request.data['reject_message']

        serializer = AppointmentUpdateStatusByIdSerializers(appointmentToUpdate, data = model_to_dict(newAppointment))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)