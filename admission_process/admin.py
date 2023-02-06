from django.contrib import admin
from .models import Appointment, AdmissionApplication


admin.site.register(AdmissionApplication)
admin.site.register(Appointment)