from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from accounts.models import StudentProfile



class Attendance(models.Model):

    STATUS = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Excused', 'Excused'),
    )

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'attendances')
    date = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS, default='Present')
    lesson_period = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(7)],
    )

