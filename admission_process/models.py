from django.db import models
from school_process.models import Class



class AdmissionApplication(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    STATUS = (
        ('Received', 'Received'),
        ('Appointment', 'Appointment'),
    )
    student_first_name = models.CharField(max_length=55)
    student_last_name = models.CharField(max_length=55)
    health_insurance = models.CharField(max_length=55)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25, choices=GENDER)
    email = models.EmailField()
    year_of_entry = models.CharField(max_length=25)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    period = models.CharField(max_length=25)
    surname_doe = models.CharField(max_length=55)
    guardian_first_name = models.CharField(max_length=55)
    guardian_last_name = models.CharField(max_length=55)
    guardian_address = models.CharField(max_length=255)
    home_phone_no = models.CharField(max_length=25)
    guardian_mobile_no = models.CharField(max_length=25)
    previous_school_name = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    starting_date = models.DateField()
    departure_date = models.DateField()
    notes = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Received')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    