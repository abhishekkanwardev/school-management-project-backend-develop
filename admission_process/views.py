from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Class, AdmissionApplication
from .serializers import ClassSerializer, AdmissionApplicationSerializer
from rest_framework.permissions import AllowAny



class ClassViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    

class AdmissionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = AdmissionApplication.objects.all()
    serializer_class = AdmissionApplicationSerializer