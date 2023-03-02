from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Class, AdmissionApplication
from .serializers import ClassSerializer, AdmissionApplicationSerializer, AppointmentSerializers, AppointmentUpdateStatusByIdSerializers, AdmissionApplicationNonAuthSerializer
from rest_framework.permissions import AllowAny
from .permission import IsAdminUser
from .models import Appointment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from copy import copy
from datetime import date

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


class AdmissionApplicationNonAuthDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        application_instance = get_object_or_404(AdmissionApplication, pk=pk)
        return application_instance
        
    def get(self, request, pk):
        application = self.get_object(pk = pk)
        serializer = AdmissionApplicationNonAuthSerializer(application)
        return Response(serializer.data)


class AppointmentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

    def get_serializer_context(self):
        return {"request": self.request}


class AppointmentTimeAvailableStateList(APIView):

    def get(self, request, year, month, day):
        filteredDataQuery = Appointment.objects.filter(appointment_date__year=year, appointment_date__month=month, appointment_date__day=day)
        timeslots = Appointment.TIMESLOT_LIST
        timeAvailableList = list()

        for timeslot in timeslots:
            isExistData = False
            if filteredDataQuery:
                isExistData = filteredDataQuery.filter(appointment_time = timeslot[0], status = 'Accept').exists()
            timeAvailableList.append({'id':timeslot[0], 'value': timeslot[1], 'is-available': not isExistData})

        return Response(timeAvailableList)
    

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

        elif appStatus == 'Accept':
            newAppointment.reject_message = None

            admission = appointmentToUpdate.admission_application
            admissionStatus = admission.status
            index = 0
            statusList = AdmissionApplication.STATUS
            for status in statusList:
                if admissionStatus in status:
                    index = statusList.index(status)
                    break

            admission.status = statusList[index+1][0]
            admission.save()


        serializer = AppointmentUpdateStatusByIdSerializers(appointmentToUpdate, data = model_to_dict(newAppointment))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
            
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    

class AppointmentNonAuthPostAPIView(APIView):
    permission_classes = [AllowAny]
         
    def post(self, request):
        serializer = AppointmentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  
        #status change 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

